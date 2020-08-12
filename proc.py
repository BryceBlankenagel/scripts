#!/usr/bin/env python3

from datetime import datetime
import html
import unicodedata, re, io

def slugify(value):
    """
    Converts to lowercase, removes non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)

#f = open("Untitled spreadsheet - Sheet2.tsv", "r")
f = io.open("Namo Episodes - Sheet2 (3).tsv", "r", encoding="utf-8")
f.readline() # headers

for line in f:
    title, category, url, filename, lurl, date1, date2 = line.split('\t')
    realdate=datetime.strptime(date2.strip(), '%m/%d/%Y %H:%M:%S')
    #print(title, url, realdate)
    if filename!="":
        outfile =  '-'.join([realdate.strftime('%Y-%m-%d'), slugify(unicode(title))]) + '.markdown'
        frontmatter=u'''---
layout: post
title: >
    {title}
episode_url: {url}
libsyn_url: {lurl}
category: {category}
date: {date}
---

'''.format(title=title,url=url,lurl=lurl,category=category,date=realdate.strftime('%Y-%m-%d %H:%M:%S +0000'))

        print ("doing ", title)
        o=io.open('output/'+outfile, "w", encoding='utf-8')
        gen=io.open(filename, 'r', encoding='utf-8')
        o.write(frontmatter)
        o.write(gen.read())
        gen.close()
        o.close()


