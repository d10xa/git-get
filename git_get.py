#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
from collections import namedtuple
from os.path import expanduser

from subprocess import call

GitUrl = namedtuple('GitUrl', 'host, group, org, repo, url')


def main():
    url = sys.argv[1]
    git_url = parse_git_url(url)

    if git_url.group:
        directory = os.path.join(expanduser("~"), git_url.host, git_url.group, git_url.org, git_url.repo)
    else:
        directory = os.path.join(expanduser("~"), git_url.host, git_url.org, git_url.repo)

    if not os.path.exists(directory):
        os.makedirs(directory)

    call(["git", "clone", git_url.url, directory])


def parse_git_url(s):
    r = re.search('^git@(.+):(.+)/(.+)/(.+).git$', s)
    if r:
        return GitUrl(host=r.group(1), group=r.group(2), org=r.group(3), repo=r.group(4), url=s)

    r = re.search('^git@(.+):(.+)/(.+).git$', s)
    if r:
        return GitUrl(host=r.group(1), group=None, org=r.group(2), repo=r.group(3), url=s)

    r = re.search('^https://(.+)/(.+)/(.+)/(.+).git$', s)
    if r:
        return GitUrl(host=r.group(1), group=r.group(2), org=r.group(3), repo=r.group(4), url=s)

    r = re.search('^https://(.+)/(.+)/(.+).git$', s)
    if r:
        return GitUrl(host=r.group(1), group=None, org=r.group(2), repo=r.group(3), url=s)

    r = re.search('^https://(.+)/(.+)/(.+)/(.+)', s)
    if r:
        return GitUrl(host=r.group(1), group=r.group(2), org=r.group(3), repo=r.group(4), url=s + ".git")

    r = re.search('^https://(.+)/(.+)/(.+)', s)
    if r:
        return GitUrl(host=r.group(1), group=None, org=r.group(2), repo=r.group(3), url=s + ".git")

    r = re.search('(.+)/(.+)', s)
    if r:
        url = 'https://github.com/' + r.group(1) + "/" + r.group(2) + '.git'
        return GitUrl(host="github.com", group=None, org=r.group(1), repo=r.group(2), url=url)
    else:
        return None


if __name__ == '__main__':
    main()
