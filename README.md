# Show Scripts github pages site

If you find an error on the site, please sumit a correction!

Each file in the `_posts` directory constitutes the show notes for an episode. Bryce prepares show notes ahead of time, and they make their way into this github repository for all to access. If there is a typo, or other fix/enhancement that could be submitted, those submissions are welcome. Submitting a pull request that significantly alters the notes will be rejected, but minor corrections such as typo fixes or adding hyperlinks are generally welcome. Anything more than a minor correction may not be accepted unless cleared ahead of time!

To contribute a correction, you will need a github account, which is free. Each page has a link near the bottom that says "Edit this page on github". This will open an editor for logged-in github users, and prompt you to make changes, and then create a pull request. Pull Requests will be reviewed and accepted or rejected.

# Technical info about the website

This is a jekyll website. The show notes were converted from their original .docx or .odt to be github-flavored markdown format. This was done with a tool called pandoc.

    for i in *; do pandoc -t gfm -f $i -o $i.markdown; done

Jekyll can be used for dated content posts such as a blog. The post functionality is what is used here. Jekyll posts and pages have a section at the top of the file called the frontmatter. The frontmatter has information about the post that can be used when the content is rendered for display. Each post has front matter as follows:

    ---
    layout: post
    title: >
        Ep 6 - Polygamy Special
    episode_url: https://nakedmormonismpodcast.com/episode-6-polygamy-special-pt-1/
    libsyn_url: https://nakedmormonismpodcast.libsyn.com/ep6-polygamy-special
    category: History
    date: 2014-11-21 05:29:25 +0000
    ---

The `layout: post` bit tells jekyll to render it as a post explicitly. The `title` bit has a `>` and the actual title appears on the next line.

The episode_url and libsyn_url are fields specifically created with this project in mind. episode_url is utilized to generate the link back to the show at the top. The libsyn data was also present, so I figured I would include it.

The process I used for getting all the frontmatter data put together was to gather all the needed info into a spreadsheet and then feed that into a script that would write out the files.

To get started, I populated data from the RSS feed of the show. I used the `=IMPORTFEED("https://nakedmormonismpodcast.libsyn.com/rss", "items", true, 250)` function in google sheets. 250 was the max, which meant a few episodes were left out and I had to grab that data by hand.

This got me the Title, libsyn URL, and the date created. I threw away the summary field from the RSS feed.

I downloaded each page from https://nakedmormonismpodcast.com/history/ and parsed out all the links across those pages. I ended up manually ordering them, and then I pasted those URLs for each episode in a new column in the spreadsheet. This became the episode_url.

I did a similar ordering process for the show notes filenames, and that became the "filename" field. I also manually write the Category for each episode so I could use google sheets to filter down to only the Historical episodes. (the RSS feed had all episodes)

At this point, I edited some of the titles for some consistency in naming. I also set the filename to 'todo' or 'none' for some of the episodes. These ended up being actual filenames that had boilerplate "There are no notes" or whatnot.

When the spreadsheet had the Title, Category, URL, filename, libsyn url, and datetime stamp, I exported it to a tab delimited file (tsv) from google sheets and fed that into a python script I wrote.

This `proc.py` script is included in the repository, but is not meant to be used over and over. Basically, it looks at every line that it is fed, it extracts all the information, decides what the filename should be for the jekyll post, writes all the front matter, and then tosses in the previously converted markdown.
