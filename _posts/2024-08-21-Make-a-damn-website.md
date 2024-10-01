---
title: Go make a website
date: 2024-08-21
tags: ramble
---

**TL;DR I'm lazy and just want to steal your website.**

[Sure, go ahead](https://github.com/davidquarel/davidquarel.github.io). I took all the boilerplate
from [Shawn Ligocki](https://www.sligocki.com/), so it's only fair. Don't forget to delete `_posts`
and edit `_config.yml` to have your own details.


{% include bar.html %}


It's 2024, LLMs are a thing, and they'll (very politely and 
with infinite patience for dumb questions) hand-hold you through the process 
of making a website.
That's what I did, and am currently doing. I'm not a web developer by any 
stretch of the imagination, but I can make a website that looks like it was 
made by someone who knows what they're doing. 


**How?**

I literally just asked 
GPT-4 "I want a website where I write markdown files and it turns them 
into blog posts" and it spat out a bunch of instructions
for "install Ruby and [Jekyll](https://jekyllrb.com/)" and 
"use [GitHub pages](https://pages.github.com/)" and 
"here's where you get [templates](https://jekyllrb.com/docs/themes/)" 
and such and such. Worked a treat!

**Okay, how do I do it?**

I got halfway through writing a guide for how to set up a Jekyll blog and host it on GitHub Pages,
but then I realised that Claude would probably do a better job of it (especially as that's what I did in the first place),
so I just asked it to write the guide for me too. Here's what it came up with:

<details markdown="block">
<summary> How do I set up a Jekyll blog and host it on GitHub Pages? (by Claude) </summary>

0. Be on Linux or Mac. If you're on Windows, consider using [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem for Linux). After setting up WSL, you can follow the Linux instructions.

1. Install Ruby
   * Windows (if not using WSL): [RubyInstaller](https://rubyinstaller.org/)
   * Mac: `brew install ruby`
   * Linux (and WSL): 
     ```
     sudo apt-get update
     sudo apt-get install ruby-full
     ```
   Verify the installation with `ruby --version` and `gem --version`.

2. Install Jekyll and create a new site
   ```
   gem install jekyll bundler
   jekyll new my-awesome-site
   cd my-awesome-site
   bundle exec jekyll serve
   ```
   Then visit `http://localhost:4000` in your browser to see your site.

3. Write a blog post
   * Create a new file in the `_posts/` directory
   * Name it `YYYY-MM-DD-title.md` (e.g., `2024-08-21-my-first-post.md`)
   * Write your post content in Markdown format

4. Preview your changes locally
   * Run `bundle exec jekyll serve`
   * Visit `http://localhost:4000` in your browser
   * The site will automatically update when you save changes to your files

5. Set up GitHub Pages
   * Create a new GitHub repository named `username.github.io` (replace `username` with your GitHub username)
   * Initialize git in your local Jekyll site directory (if not already done):
     ```
     git init
     ```
   * Add your files to git:
     ```
     git add .
     ```
   * Commit your changes:
     ```
     git commit -m "Initial commit"
     ```
   * Connect your local repository to GitHub:
     ```
     git remote add origin https://github.com/username/username.github.io.git
     ```
   * Push your changes to GitHub:
     ```
     git push -u origin main
     ```
     (Use `main` or `master` depending on your default branch name)

6. Configure GitHub Pages
   * Go to your repository on GitHub
   * Click on "Settings" > "Pages" in the left sidebar
   * Under "Source", select the branch you want to use (usually `main` or `master`)
   * Click "Save"

7. Update your site configuration
   * Open `_config.yml` in your local repository
   * Add or update the `url` field:
     ```yaml
     url: "https://username.github.io"
     ```
   * Commit and push these changes:
     ```
     git add _config.yml
     git commit -m "Update config for GitHub Pages"
     git push
     ```

8. Wait for deployment and visit your site
   * GitHub will automatically build and deploy your site (this may take a few minutes)
   * Your site should now be live at `https://username.github.io`

Remember to replace `username` with your actual GitHub username throughout these steps.

</details>

TL;DR: You install Ruby, install Jekyll, make a GitHub repo `username.github.io`, setup GitHub Pages, and then write markdown files in `_posts/` to make blog posts.
Push them, and GitHub will automatically build and deploy your site. Fantastic! No need to learn HTML, CSS, or JavaScript.

<!-- 0. Be on Linux or Mac. If you're on Windows, good luck. 
   I've heard [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) is good,
   and then you can just follow the instructions for Linux, but I haven't tried it.
1. Install Ruby
  * Windows: [RubyInstaller](https://rubyinstaller.org/)
  * Mac: `brew install ruby`
  * Linux: `sudo apt-get install ruby-full`
  Verify this worked with `gem --version`.
2. Copy-paste the boilerplate from [Jekyll](https://jekyllrb.com)
```
gem install jekyll bundler
jekyll new my-awesome-site
cd my-awesome-site
bundle exec jekyll serve~~
```
and then go to `http://localhost:4000` in your browser.
3. Write a blog post in `_posts/` with the format `YYYY-MM-DD-title.md` in markdown.
4. Run `bundle exec jekyll serve` to see your changes locally. It will automatically
    update when you save the file.
5. Make a GitHub repository with the name `username.github.io` and push your changes,
where `username` is your GitHub username. -->


**But why should I make a website?**

You need a place to put all the cool stuff you've done, and by virtue of having 
a website it'll force you to
1. Do stuff[^do_stuff].
2. Make sure that all the cool stuff you've done is actually cool (because 
it'll be there for everyone else to see).
3. Can have an easy place to point to with a list of what you did, your CV, etc.
for when you're applying for jobs, grants, or whatever.

Nobody is going to download and compile that buggy project from years ago 
if it's anything more complicated than 
```
make
./bin/my_thing_I_did
```
or
```
pip install -r requirements.txt
python3 my_thing_I_did.py
```
so it should be immediately obvious what you've done, why it's impressive, 
and all in a place that's easy for people to find.
Bonus points if it just runs in the browser[^javascript] so people can see it without 
having to download anything or run anything on their own machine. 

**I want LaTeX support!**

Okay here's where I ran into a bit of trouble working this one out to get MathJax to work,
so credit to [Shawn Ligocki](https://www.sligocki.com/), I just copied [his website](https://github.com/sligocki/sligocki.github.io),
stripped out all his content, and replaced it with mine. The specific files you want 
are [`_includes/custom-head.html`](https://github.com/sligocki/sligocki.github.io/blob/main/_includes/custom-head.html)
and [`_includes/head.html`](https://github.com/sligocki/sligocki.github.io/blob/main/_includes/head.html). Now I can include either inline LaTeX with `$$ \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} $$` which renders as: $$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$$

[^do_stuff]: Maybe this will work. Maybe it won't. No guarantees. ¯\\\_(ツ)\_/¯
[^javascript]: Sadly this will likely require some JavaScript, which I haven't learned and hope to avoid for as long as possible. 

**I want comments!**

I'm using [utterances](https://utteranc.es/) for comments, which is a neat little
GitHub issue-based commenting system. Each comment becomes an issue on your GitHub
repository, so you can manage them all in one place. You can see an example at the bottom of this page.


**Public or Private?**

If you have a GitHub Pro account, you can run GitHub Pages on private repositories.
This has the upside of being able to write drafts and have all the commented out
sections not publicly visible (view the page source to see). HTML comments are still visible
in the page source<!-- like this one! -->, so be careful with those. Comments
using the liquid syntax `{% raw %}{% comment %}...{% endcomment %}{% endraw %}`
{% comment %} like this one {% endcomment %}are not visible in the page source,
but you can still see them in the 
[raw markdown file](https://github.com/davidquarel/davidquarel.github.io/blob/60f7ea6ece718e5e64c69dca590e96b16be73668/_posts/2024-08-21-Make-a-damn-website.md?plain=1#L203) on GitHub.

The downside is that it breaks the utterances commenting system, as it can't
access the private repository. My solution is I just keep my draft posts that I'm
not working on in `_drafts`, move them to `_posts` when I'm working on them so I can render them locally,
and then push them to the repo when I want to publish them. You can also add
`published: false` to the front matter of a post to prevent the post from being
rendered if you don't mind the half-finished post being visible in the repo on GitHub.

**I want more advanced features!**

GitHub Pages is great for simple static sites like this one.
For more complex things where you want interactive demos, I've had good experiences
with [Streamlit](https://streamlit.io/): You simply write a Python script
with some in-line markdown and it turns it into a web app. 
[Callum](https://www.perfectlynormal.co.uk/) used this to
great effect for the [ARENA](https://www.arena.education/) workshop.
[Working attention patterns](https://arena3-chapter1-transformer-interp.streamlit.app/[1.1]_Transformer_from_Scratch#attention) 
in the browser is incredibly powerful
for helping participants understand the material. There's enough content
out there written in Streamlit that LLMs are pretty good at helping you
figure out how to do what you want, and often you can just write raw
markdown, and then get the LLM to wrap it in whatever Streamlit magic
is needed to make it work.

**I keep forgetting to push all my dependencies and then my site breaks!**

Worry not! I solved this problem by adding a git pre-commit hook that
scans all my posts for any untracked dependencies and prints an angry
message if it finds any. You can see the script
[here on GitHub](https://github.com/davidquarel/davidquarel.github.io/blob/main/files/pre-commit.py).
