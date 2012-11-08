#encoding:utf-8
import sys
import os
import django.conf.global_settings

try:
    from localsettings import *
except ImportError:
    print u'Укажите локальные настройки в файле localsettings.py'
    sys.exit(1)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DIRNAME = os.path.abspath(os.path.dirname(__file__))


ADMINS = (
    ('Ivan Petuhov', 'ivan@blanki.biz'),
    ('Egor Vinogradov', 'egor@blanki.biz'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'blanki.sqlite',  # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = os.path.join(DIRNAME, 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(DIRNAME, 'static')

STATIC_URL = STATICFILES_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = [
    MEDIA_ROOT,
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1mqnr8(*%t&a908^=@p%y330r6%+t*xgzj3x$0p%e!x-q2)t%$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'blanki.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DIRNAME, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'annoying',
    'south',
    'registration',
    'social_auth',
    'webodt',

    'comments',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


WEBODT_CONVERTER = 'webodt.converters.openoffice.OpenOfficeODFConverter'

PYTILS_SHOW_VALUES_ON_ERROR = False

COMMENTS_APP = 'comments'

ACCOUNT_ACTIVATION_DAYS = 7

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleBackend',
    'social_auth.backends.contrib.vkontakte.VKontakteBackend',
    'social_auth.backends.contrib.mailru.MailruBackend',
    'social_auth.backends.contrib.odnoklassniki.OdnoklassnikiBackend',
    'social_auth.backends.contrib.yandex.YaruBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TWITTER_CONSUMER_KEY = 'YoUQdTRtNaS1MKyhfbq2A'
TWITTER_CONSUMER_SECRET = '0ywaTMEUenz5PhUNU7GVya5txD4fVeCR4JSHL1mv20'
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
GOOGLE_CONSUMER_KEY = ''
GOOGLE_CONSUMER_SECRET = ''
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''
VKONTAKTE_APP_ID = '3224611'
VKONTAKTE_APP_SECRET = 'qtRWXzngtAnXzzqEitfk'
MAILRU_OAUTH2_CLIENT_KEY = ''
MAILRU_OAUTH2_CLIENT_SECRET = ''
ODNOKLASSNIKI_OAUTH2_APP_KEY = ''
ODNOKLASSNIKI_OAUTH2_CLIENT_SECRET = ''
YANDEX_APP_ID = ''
YANDEX_API_SECRET = ''

LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL = '/login-error/'

SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'


TEMPLATE_CONTEXT_PROCESSORS = \
django.conf.global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'context_processors.project_urls',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

VKONTAKTE_LOCAL_HTML = 'accounts/vkontakte.html'
