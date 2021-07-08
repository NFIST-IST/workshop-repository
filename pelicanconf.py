#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'NFIST'
SITENAME = 'workshops'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['files','images']

TIMEZONE = 'Europe/Lisbon'
LOCALE = 'pt_PT.utf8'

DEFAULT_LANG = 'en'
BANNER = "images/workshop_fc_banner.png"

CC_LICENSE = "CC-BY-SA"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOAD_CONTENT_CACHE = False

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
         # ('Python.org', 'https://www.python.org/'),
         # ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/NucleoFisicaIST','facebook-square'),
        ('Instagram','https://www.instagram.com/nfist_/','instagram'),
        ('Website','https://www.nfist.pt', 'link'),)

DEFAULT_PAGINATION = False

ARTICLE_URL = "{category}/{slug}"
ARTICLE_SAVE_AS = "{category}/{slug}.html"
PAGE_URL = "{category}/{slug}/"
PAGE_SAVE_AS = "{category}/{slug}.html"

#Plugins
PLUGIN_PATHS = ['pelican-plugins']

# MARKDOWN = ['(css_class=highlight, linenums=True)','extra']

MARKDOWN = {
        'extensions': ['markdown.extensions.codehilite'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight',
            'linenums':None,'guess_lang':False},
        'markdown.extensions.tables': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

MARKUP = ("md",)

# from pelican_jupyter import liquid as nb_liquid
from pelican_jupyter import markup as nb_markup

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGINS = [
    'i18n_subsites',
    'series',
    'tag_cloud',
    'liquid_tags.youtube',
    # 'liquid_tags.notebook',
    # 'liquid_tags.include_code',
    'render_math',
    # 'pelican-ipynb.markup' 
    nb_markup
    ]

I18N_TEMPLATES_LANG = 'en'

IGNORE_FILES = [".ipynb_checkpoints",".*"]

IPYNB_FIX_CSS = False
IPYNB_EXPORT_TEMPLATE="base"

#Theme Settings
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'sandstone'

SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
SHOW_DATE_MODIFIED = False


PYGMENTS_STYLE = 'monokai'
BOOTSTRAP_FLUID = True

SITELOGO = 'images/logo.png'
SITELOGO_SIZE = 100
HIDE_SITENAME = False

BOOTSTRAP_NAVBAR_INVERSE = False

#SERIES_TEXT = ''
DISPLAY_SERIES_ON_SIDEBAR = True
SHOW_SERIES = True

FAVICON = 'images/favicon.png'

DISPLAY_TAGS_ON_SIDEBAR = False
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
