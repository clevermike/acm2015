"""
Django settings for acm2015 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_*!2^&vyyx!2yh_@b0p4-lc@!r(brt!861-svc3c%tvyff68py'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [ '192.168.119.213',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web',
    'django_crontab',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.CacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# CACHE_MIDpDLEWARE_SECONDS = 10

ROOT_URLCONF = 'acm2015.urls'

WSGI_APPLICATION = 'acm2015.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'acm2015',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'acm2015.'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    '/var/www/acm2015/templates',
)

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'static/',
)

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#SESSION_COOKIE_AGE = 60 * 30

CRONJOBS = (
)
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
#         },
#     },
#     'filters': {
#     },
#     'handlers': {
#         'default': {
#             'level':'DEBUG',
#             'class':'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(STATIC_ROOT+'/logs/','acm2015.log'),
#             'maxBytes': 1024*1024*5, # 5 MB
#             'backupCount': 5,
#             'formatter':'standard',
#         },
#         'console':{
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default','console'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#     }
# }

