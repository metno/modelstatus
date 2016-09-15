"""
Django settings for productstatus project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import logging
import uuid
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wa^sp+--!2+t8xlb4g__%uu2oow=)#s#-fonk6ttuu^abw2wbv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'productstatus.core',
    'productstatus.check',
    'tastypie',
    'corsheaders',
    'raven.contrib.django.raven_compat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'productstatus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'productstatus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Configure logging.
#
# This configuration sets up two loggers:
#
# 1. If DEBUG=True, print all logging messages to stdout
# 2. Log every message to syslog, if priority is INFO or higher
#
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': 'productstatus[%(process)d] %(name)s (%(levelname)s) %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] %(name)s (%(levelname)s) %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'facility': 'local7',
            'address': '/dev/log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        # root logger
        '': {
            'handlers': ['console', 'syslog'],
            'level': 'DEBUG',
            'disabled': False
        },
    },
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Allow Cross-Origin Resource Sharing
CORS_ORIGIN_ALLOW_ALL = True

# Detect test mode
TESTING = sys.argv[1:2] == ['test']

# TastyPie settings
TASTYPIE_DEFAULT_FORMATS = ['json']

# Kafka settings
KAFKA_SINGLETON_PK = 'default'
KAFKA_BROKERS = ['localhost:9092']
KAFKA_CLIENT_ID = 'productstatus-' + str(uuid.uuid4())
KAFKA_TOPIC = 'productstatus'
KAFKA_REQUEST_TIMEOUT = 2000  # milliseconds
KAFKA_SSL = False
KAFKA_SSL_VERIFY = True
KAFKA_HEARTBEAT_INTERVAL = 60  # seconds

# Frontend date/time format
DATETIME_FORMAT = 'Y-m-d H:i:s\Z'

# Reflection when generating resource URLs
PRODUCTSTATUS_HOST = 'localhost:8000'
PRODUCTSTATUS_BASE_PATH = '/api/v1'
PRODUCTSTATUS_PROTOCOL = 'http'

# Blank Raven configuration, please configure in local_settings
RAVEN_CONFIG = {}

# Import site-specific (production) settings, overwriting any local default variables
try:
    from .local_settings import *
except ImportError:
    logging.warning("Failed to import local_settings, continuing with defaults")
