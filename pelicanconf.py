#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Deepak Ramanath'
SITENAME = u'Deepak Ramanath'
SITEURL = ''
COPYRIGHT_YEAR = 2018
PATH = 'content'
TIMEZONE = 'Australia/Sydney'
DEFAULT_LANG = u'en'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Blogroll
LINKS = (('Python | Linux', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://au.linkedin.com/in/deepakramanath'),
          ('github', 'https://github.com/deepakramanath'),
          ('gitlab', 'https://gitlab.com/deepakramanath'),
          ('twitter', 'https://twitter.com/deepakramanath'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "themes/Flex"

# Theme customization
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
