"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

try:
    from myproject import local_settings
except ImportError:
    raise ImproperlyConfigured(
        "Configuration file is not present. Please define myproject/myproject/local_settings.py"
    )

SECRET_KEY = getattr(local_settings, 'DJANGO_SECRET_KEY', None)
STATIC_ROOT = getattr(local_settings, 'DJANGO_STATIC',  os.path.join(BASE_DIR, 'static'))
MEDIA_ROOT = getattr(local_settings, 'DJANGO_MEDIA',  os.path.join(BASE_DIR, 'media'))
HOSTNAME = getattr(local_settings, 'HOSTNAME')

REDIS_HOST = getattr(local_settings, 'REDIS_HOST', 'localhost')
REDIS_PORT = getattr(local_settings, 'REDIS_PORT', 6379)
REDIS_DATABASE = getattr(local_settings, 'REDIS_DATABASE', 0)
REDIS_PASSWORD = getattr(local_settings, 'REDIS_PASSWORD', None)

POSTGRESQL_ENGINE = getattr(local_settings, 'POSTGRESQL_ENGINE', 'postgresql_psycopg2')
POSTGRESQL_HOST = getattr(local_settings, 'POSTGRESQL_HOST', 'localhost')
POSTGRESQL_PORT = getattr(local_settings, 'POSTGRESQL_PORT', '5432')
POSTGRESQL_DB = getattr(local_settings, 'POSTGRESQL_DB')
POSTGRESQL_USERNAME = getattr(local_settings, 'POSTGRESQL_USERNAME')
POSTGRESQL_PASSWORD = getattr(local_settings, 'POSTGRESQL_PASSWORD')

RABBITMQ_HOST = getattr(local_settings, 'RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = getattr(local_settings, 'RABBITMQ_PORT', '5672')
RABBITMQ_VHOST = getattr(local_settings, 'RABBITMQ_VHOST', 'celery')
RABBITMQ_USERNAME = getattr(local_settings, 'RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = getattr(local_settings, 'RABBITMQ_PASSWORD')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
if HOSTNAME:
    DEBUG = False
    ALLOWED_HOSTS = [HOSTNAME]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',

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

ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.{}'.format(POSTGRESQL_ENGINE),
        'NAME': POSTGRESQL_DB,
        'USER': POSTGRESQL_USERNAME,
        'PASSWORD': POSTGRESQL_PASSWORD,
        'HOST': POSTGRESQL_HOST,
        'PORT': POSTGRESQL_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


MEDIA_URL = '/media/'


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': [
            '{}:{}'.format(REDIS_HOST, REDIS_PORT)
        ],
        'OPTIONS': {
            "DB": REDIS_DATABASE,
        }
    },
}

BROKER_URL = 'amqp://{}:{}@{}:{}/{}'.format(RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_VHOST)
