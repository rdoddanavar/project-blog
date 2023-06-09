AUTHOR = 'Roshan Doddanavar'
SITENAME = 'Roshan\'s Personal Blog'
SITEURL = 'http://localhost:8000/'

PATH = 'content'

TIMEZONE = 'America/Phoenix'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/roshan-doddanavar'),
          ('github', 'https://github.com/rdoddanavar'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#------------------------------------------------------------------------------#

# USER SETTINGS

USE_FOLDER_AS_CATEGORY = True

STATIC_PATHS = ['images']

#------------------------------------------------------------------------------#

# THEME SETTINGS

THEME = '/home/roshan/GitHub/minimal-xy'

# Author
AUTHOR_INTRO = 'Hello, I\'m Roshan - a professional Aerospace Engineer, and an avid hobbyist & tinkerer.'
AUTHOR_AVATAR = 'images/headshot.jpg' # Must be relative to content/ directory

# Theme customizations


# UNUSED

#THEME = 'pelican-bootstrap3'
#THEME = 'taman'

#THEME = 'uikit'
#DISPLAY_LINKS_ON_SIDEBAR_LIMIT = 3
#DISPLAY_TAGS_ON_SIDEBAR_LIMIT = 3
#LICENSE = "None"