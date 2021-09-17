#!/usr/bin/env python
from __future__ import print_function

import glob
import os
import re


project_dir = os.path.abspath(os.path.dirname((os.path.dirname(__file__))))
post_dir = os.path.join(project_dir, "_posts")
tag_dir = os.path.join(project_dir, "tags")
crawl_re = re.compile(r"^\s*\-+\s*$")
tags_re = re.compile(r"^\s*tags:.+$")

filenames = glob.glob(os.path.join(post_dir, "*.md"))
total_tags = set()
for filename in filenames:
    with open(filename, "r") as f:
        crawl = False
        for line in f:
            if crawl_re.match(line):
                if crawl:
                    break
                crawl = True
            if crawl:
                if not tags_re.match(line):
                    continue
                current_tags = line.strip().split()
                for t in current_tags[1:]:
                    t = t.strip()
                    if t:
                        total_tags.add(t)
                break

old_tags = glob.glob(os.path.join(tag_dir, "*.md"))
for tag in old_tags:
    os.remove(tag)

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

tagContextTpl = """---
layout: tagpage
title: "Tag: {0}"
tag: {0}
robots: noindex
---
"""

for tag in total_tags:
    tag_filename = os.path.join(tag_dir, tag + ".md")
    f = open(tag_filename, "a")
    write_str = tagContextTpl.format(tag)
    f.write(write_str)
    f.close()
print("Tags generated, count", len(total_tags))
