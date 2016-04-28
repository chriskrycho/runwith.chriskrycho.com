#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Krycho'
SITENAME = 'Run With Me: A Micro-Podcast About Running'
SITE_DESCRIPTION = 'Run With Me is a microcast about running, recorded while running. In 3–5 minute episodes, released weekly-ish, I talk about it all: ups and downs, training, health, nutrition, motivation, racing, weird things your body does on long runs—everything.'
SITEURL = ''

LOGO = '//cdn.chriskrycho.com/runwith/cover-web.jpg'

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_DATE_FORMAT = "%B %d, %Y"
DEFAULT_LANG = 'en'

THEME = 'podcast_theme'

THEME_STATIC_DIR = ''

# No categories or tags
DIRECT_TEMPLATES = ['index', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['archives']

ARTICLE_SAVE_AS = '{category}/{number}/index.html'
ARTICLE_URL = '{category}/{number}/'

ARCHIVES_SAVE_AS = 'all/index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

# Disable unused pages
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''


# All feeds for this particular site are disabled; I generate the feeds via
# [Feeder] -- at least until such a time I create a podcast plugin for Pelican.
# (Frankly, that might be never.)
#
# [Feeder]: http://reinventedsoftware.com/feeder/
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 12  # roughly 3 months. Ish.

STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/feed.xml': {'path': 'feed.xml'},
                       'extra/.nojekyll': {'path': '.nojekyll'}}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
