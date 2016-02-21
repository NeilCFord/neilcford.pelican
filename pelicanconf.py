#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Neil C Ford'
SITENAME = 'Neil C Ford'
SITEURL = 'http://neilcford.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'

STATIC_PATHS = ['images', 'static', 'keybase.txt']

DEFAULT_LANG = 'en'

THEME = '/Users/neil/git/neilcford.pelican/crowsfoot'

PROFILE_IMAGE_URL = 'http://neilcford.uk/images/Neil_crop160px.jpg'

TYPOGRIFY = True

EMAIL_ADDRESS = 'neil@neilcford.uk'
GITHUB_ADDRESS = 'https://github.com/neilcford'
TWITTER_ADDRESS = 'https://twitter.com/neilcford'

MENUITEMS = [('Home', '/')]

# feed
FEED_RSS = 'feeds/rss.xml'
FEED_MAX_ITEMS = 10

SHOW_ARTICLE_AUTHOR = False

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
