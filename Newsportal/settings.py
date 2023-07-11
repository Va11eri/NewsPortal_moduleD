"""
Django settings for Newsportal project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import logging
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-p2tr)g+1g)7q_7_e87r8x2*)(g$x0-ivg^7)$8gs9ml%*w#$ey'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
   # 'News.apps.NewsConfig',
    'News',
    'sign',
    'protect',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'modeltranslation',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'Newsportal.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Newsportal.wsgi.application'
LOGIN_REDIRECT_URL = '/news/'
LOGIN_URL = '/accounts/login/'
LOGOUT_REDIRECT_URL = '/news/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_FORMS = {'signup': 'News.forms.BasicSignupForm'}

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Русский'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR / 'static']

EMAIL_HOST = 'smtp.mail.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'mynewsportal@mail.ru'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = 'd7s9ePcyEiqrDSNhdR7Y' # пароль от почты
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'mynewsportal@mail.ru'
SITE_URL = 'http://127.0.0.1:8000'
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25
CELERY_BROKER_URL = 'redis://:CSvycAbSZfX2gQGuqMaAs2W7gflznEPu@redis-10627.c90.us-east-1-3.ec2.cloud.redislabs.com:10627'
CELERY_RESULT_BACKEND = 'redis://:CSvycAbSZfX2gQGuqMaAs2W7gflznEPu@redis-10627.c90.us-east-1-3.ec2.cloud.redislabs.com:10627'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "filters": ["console_only"],
        },
        "general_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/general.log",
            "maxBytes": 1048576,  # 1MB
            "backupCount": 10,
            "formatter": "simple",
            "filters": ["email_file_only"],
        },
        "errors_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/errors.log",
            "maxBytes": 1048576,  # 1MB
            "backupCount": 10,
            "formatter": "verbose",
            "filters": ["email_file_only"],
        },
        "security_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "logs/security.log",
            "maxBytes": 1048576,  # 1MB
            "backupCount": 10,
            "formatter": "verbose",
            "filters": ["email_file_only"],
        },
        "mail_admins": {
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": True,
            "filters": ["email_file_only"],
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "general_file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["errors_file", "mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["errors_file", "mail_admins"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.template": {
            "handlers": ["errors_file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["errors_file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["security_file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "filters": {
        "console_only": {
            "()": "django.utils.log.CallbackFilter",
            "callback": lambda record: settings.DEBUG,
        },
        "email_file_only": {
            "()": "django.utils.log.CallbackFilter",
            "callback": lambda record: not settings.DEBUG,
        },
    },
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(message)s",
        },
        "simple": {
            "format": "%(asctime)s %(levelname)s [%(module)s] %(message)s",
        },
    },
}

