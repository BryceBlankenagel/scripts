#!/usr/bin/env python3

from datetime import datetime
import html

#f = open("Untitled spreadsheet - Sheet2.tsv", "r")
f = open("Namo Episodes - Sheet2 (1).tsv", "r")
f.readline() # headers

for line in f:
    title, category, url, filename, lurl, date1, date2 = line.split('\t')
    realdate=datetime.strptime(date2.strip(), '%m/%d/%Y %H:%M:%S')
    #print(title, url, realdate)
    if filename!="":
        outfile =  '-'.join([str(realdate.year), str(realdate.month), str(realdate.day)] +  title.lower().split(' ')[:2]) + '.markdown'
        frontmatter='''---
layout: post
title: >
    {title}
episode_url: {url}
libsyn_url: {lurl}
category: History
date: {date}
---

'''.format(title=html.escape(title),url=url,lurl=lurl,date=realdate.strftime('%Y-%m-%d %H:%M:%S +0000'))

        print ("doing ", title)
        o=open('output/'+outfile, "w")
        gen=open(filename, 'r')
        o.write(frontmatter)
        o.write(gen.read())
        gen.close()
        o.close()


