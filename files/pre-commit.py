#!/usr/bin/env python3
import os
import re
import sys
import subprocess
from pathlib import Path

"""
Pre-commit Hook for Untracked Dependency Checking

This script serves as a pre-commit hook for Git, designed to check for untracked
dependencies in markdown files within the _posts directory of a Jekyll-based website.

Features:
- Scans markdown files in _posts/ for potential dependencies (images, links, etc.)
- Checks if these dependencies are tracked by Git
- Provides options to debug or force commit if untracked dependencies are found

Usage:
1. Place this script in .git/hooks/pre-commit
2. Make the script executable: chmod +x .git/hooks/pre-commit

Commit Options:
- Normal commit (with dependency check):
  git commit -m "Your commit message"

- Debug mode (shows detailed checking process):
  GIT_PRECOMMIT_DEBUG=1 git commit -m "Your commit message"

- Force commit (bypass dependency check):
  GIT_PRECOMMIT_FORCE=1 git commit -m "Your commit message"

Note: This script requires Python 3 and should be run in the root directory of your Git repository.

Author: Claude 3.5 Sonnet
Last Updated: 2024-08-22
"""

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def print_blue(text):
    print(f"\033[94m{text}\033[0m")

def print_yellow(text):
    print(f"\033[93m{text}\033[0m")

def get_markdown_files():
    repo_root = os.getcwd()
    return list(Path(repo_root).glob("_posts/*.md"))

def extract_dependencies(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    dependencies = []
    patterns = [
        (r'!\[.*?\]\((.*?)\)', 'Markdown image'),
        (r'<img.*?src=["\'](.*?)["\'].*?>', 'HTML image'),
        (r'{%\s*link\s+(.*?)\s*%}', 'Jekyll link'),
        (r'\[.*?\]\((.*?)\)', 'Markdown link'),
        (r'{%\s*include\s+(.*?)\s*%}', 'Jekyll include')
    ]
    for i, line in enumerate(content, 1):
        for pattern, dep_type in patterns:
            for match in re.finditer(pattern, line):
                dependencies.append((i, match.group(1), dep_type))
    return dependencies

def get_untracked_files():
    result = subprocess.run(['git', 'ls-files', '--others', '--exclude-standard'], 
                            capture_output=True, text=True)
    return set(result.stdout.splitlines())

def escape_regex_chars(s):
    return re.escape(s).replace(r'\*', '.*')

def is_untracked(dep, untracked_files, debug=False):
    if debug:
        print_blue(f"Checking dependency: {dep}")
    if dep.startswith(('http://', 'https://', '#')):
        if debug:
            print_blue("  Skipping: external link or anchor")
        return False
    if "404.html" in dep:
        if debug:
            print_blue("  Skipping: contains 404.html")
        return False
    if dep.startswith('{%') and dep.endswith('%}'):
        dep = dep.strip('{%').strip('%}').strip().split()[-1]
        if debug:
            print_blue(f"  Extracted from Jekyll link: {dep}")
    dep = dep.lstrip('/')
    dep_pattern = escape_regex_chars(dep)
    possible_paths = [
        dep_pattern,
        os.path.join(escape_regex_chars('assets'), dep_pattern),
        os.path.join(escape_regex_chars('files'), dep_pattern),
        os.path.join(escape_regex_chars('_includes'), dep_pattern),
    ]
    if debug:
        print_blue("  Checking against patterns:")
        for path in possible_paths:
            print_blue(f"    - {path}")
    for untracked_file in untracked_files:
        if any(re.match(f'^{path}$', untracked_file) for path in possible_paths):
            if debug:
                print_blue(f"  Found match: {untracked_file}")
            return True
    if debug:
        print_blue("  No match found")
    return False

def main():
    # Check for DEBUG or FORCE environment variables
    debug = os.environ.get('GIT_PRECOMMIT_DEBUG') == '1'
    force = os.environ.get('GIT_PRECOMMIT_FORCE') == '1'

    markdown_files = get_markdown_files()
    untracked_files = get_untracked_files()
    untracked_deps = []

    if debug:
        print_blue("Untracked files:")
        for file in untracked_files:
            print_blue(f"  - {file}")

    for file_path in markdown_files:
        dependencies = extract_dependencies(file_path)
        relative_path = os.path.relpath(file_path)
        for line_num, dep, dep_type in dependencies:
            if is_untracked(dep, untracked_files, debug):
                untracked_deps.append(f"{relative_path}:{line_num}:{dep}")

    if untracked_deps:
        print_red("Warning: Untracked dependencies found.")
        print_red("The following untracked dependencies were found:")
        for dep in untracked_deps:
            print_red(dep)
        
        if not force:
            print_yellow("\nOptions:")
            print_yellow("1. To see more details about the checking process, use debug mode:")
            print_yellow("   GIT_PRECOMMIT_DEBUG=1 git commit -m 'Your message'")
            print_yellow("\n2. To force this commit and proceed despite untracked dependencies, use:")
            print_yellow("   GIT_PRECOMMIT_FORCE=1 git commit -m 'Your message'")
            sys.exit(1)
        else:
            print_blue("Proceeding with commit despite untracked dependencies.")
    else:
        print_blue("No untracked dependencies found.")
    
    sys.exit(0)

if __name__ == "__main__":
    main()