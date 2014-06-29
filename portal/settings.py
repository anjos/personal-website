# Django settings for my personal webpage

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SEND_BROKEN_LINK_EMAILS = True
import os
from dbconfig import DATABASES

# These locations are calculated based on the settings.py location
INSTALLDIR = os.path.dirname(__file__)
BASEDIR = os.path.dirname(INSTALLDIR)

# mail settings for adminstration and management bussiness
ADMINS = (
    ('Andre Anjos', 'andre.dos.anjos@gmail.com'),
)
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL = '%s <%s>' % ADMINS[0]

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/current/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'
# Valid languages for this website
gettext = lambda s: s
LANGUAGES = (
  ('en', gettext('English')),
  ('pt-br', gettext('Brazilian Portuguese')),
  ('fr', gettext('French')),
  )
DEFAULT_LANGUAGE = 1

SITE_ID = 1

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASEDIR, 'media')

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASEDIR, 'static')
STATICFILES_DIRS = ( '%s/static' % INSTALLDIR, )

# The default url for logging into the site
LOGIN_URL = '/login/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'wk&_+uqn)()=fz07y0qdl%@=m^gp^taf$&7ql&@-ffjk9aln_7'

# What we like to have in every page we render, as context
TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.debug',) \
    if DEBUG else ()
TEMPLATE_CONTEXT_PROCESSORS += (
  'django.contrib.auth.context_processors.auth', #for users and permissions
  'django.core.context_processors.i18n', #for LANGUAGES
  #'django.core.context_processors.media', #for MEDIA_URL
  #'django.core.context_processors.static', #for STATIC_URL
  'django.core.context_processors.request', #for request on every page
  'portal.context_processors.site', #for site
  'portal.context_processors.full_path', #for the full_path
  'nav.context_processors.navigation', #for our menus
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'maintenancemode.middleware.MaintenanceModeMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django_openid_auth.auth.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'portal.urls'

TEMPLATE_DIRS = (
  '%s/templates' % INSTALLDIR,
  '%s/templates/portal' % INSTALLDIR,
)

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.sites',
  'django.contrib.admin',
  'django.contrib.staticfiles',
  # 'django.contrib.sitemaps',

  # External applications reused
  'djangoogle',
  'nav',
  'bitrepo',
  'flatties',
  'chords',

  # Other applications
  'robots',
  'django_openid_auth',
)

# Controls how many albums per page to see
DJANGOOGLE_ALBUMS_PER_PAGE = 8

# Disables the sitemap functionality for robots
ROBOTS_USE_SITEMAP = False

# Enables filesystem caching
CACHES = {
    'default': {
      'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
      'LOCATION': os.path.join(BASEDIR, 'cache'),
      },
    }

# Edit this if you want to cache the whole site and use the cache middleware
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True # only for outsiders

# We keep 50% of robot data, for statistics
AUDIT_KEEP_BOT_STATISTICS = 0.5

# Which server do we authenticate against
OPENID_SSO_SERVER_URL = 'https://www.google.com/accounts/o8/id'
# Allow admins to login using this system
OPENID_USE_AS_ADMIN_LOGIN = True
# You may need this to establish your connection with Google for a start
# OPENID_CREATE_USERS = True

# For the maintenance mode middleware
#MAINTENANCE_MODE = True

# For the translations
LOCALE_PATHS = (
    os.path.join(INSTALLDIR, 'locale'),
    )
