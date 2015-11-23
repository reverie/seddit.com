from root_dir import root_dir

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASE_HOST = ''

#ADMINS = (
# ...
#)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'yoursecretkey'

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'redditchat'
DATABASE_USER = 'redditchat'
DATABASE_PASSWORD = 'yourpassword'
DATABASE_PORT = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    root_dir('templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'core.middleware.SignedAuthMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    #"django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    #"django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    'common.context.settings'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.admin',
    #'django.contrib.admindocs',
    #'multiauth',
    'core',
    'south'

)

LOG_DIRECTORY = '/project/redditchat/log'

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'server@seddit.com'

FACEBOOK_API_KEY = '...'
FACEBOOK_SECRET_KEY = '...'

TWITTER_CONSUMER_KEY = '...'
TWITTER_CONSUMER_SECRET = '...'

# Coupled with static version in index.html
REDDITCHAT_AUTH_THREAD = 'https://www.reddit.com/r/seddit_auth/comments/3btfc7/authentication_thread/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

try:
    from stagesettings import *
except ImportError:
    pass

try:
    from localsettings import *
except ImportError:
    pass
