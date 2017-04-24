"""
Django settings for mfctracker project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os.path as op
import os
from django.utils.crypto import get_random_string

import environ

GLOBAL_ENV = '/usr/local/etc/mfctracker.env'
LOCAL_ENV = 'env'

root = environ.Path(__file__) - 3 # three folder back (/a/b/c/ - 3 = /)
env = environ.Env()

SECRET_KEY = env('SECRET_KEY', default=get_random_string(length=40))

if os.path.exists(GLOBAL_ENV):
       environ.Env.read_env(GLOBAL_ENV)
if os.path.exists(root(LOCAL_ENV)):
       environ.Env.read_env(root(LOCAL_ENV))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = root()

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'bootstrap3',
    'mfctracker',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mfctracker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mfctracker.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    op.join(BASE_DIR, "static"),
]

LOGIN_REDIRECT_URL = '/'

SVN_EMAIL_DOMAIN = 'freebsd.org'
SVN_BASE_URL = 'http://svn.freebsd.org/base'
VIEWVC_REVISION_URL = 'http://svnweb.freebsd.org/changeset/base/{revision}'

TEST_RUNNER = 'django_pytest.test_runner.TestRunner'

EMAIL_CONFIG = env.email_url('EMAIL_URL', default='smtp://localhost:25')

vars().update(EMAIL_CONFIG)

DATABASES = {
    'default': env.db(default='pgsql://mfctracker@localhost/mfctracker'),
}
