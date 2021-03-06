"""
Django settings for launch_pad project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xdhcs70th#+-5^806!%($m*v_h)0glaf*xo9ly%ntrboskyg^&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['blooming-spire-6192.herokuapp.com','castlemilk.ddns.net','ukitchn.com']


# Application definition
SITE_ID = 1
INSTALLED_APPS = [
    'autocomplete_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'finance',
    'difference',
    'fuel_price',
    'word_generator',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'launch_pad.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                os.path.join(BASE_DIR, 'finance','templates'),
                os.path.join(BASE_DIR, 'difference','templates'),
                os.path.join(BASE_DIR, 'fuel_price','templates'),
                os.path.join(BASE_DIR, 'word_generator','templates'),


                ],
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

WSGI_APPLICATION = 'launch_pad.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# Parse database configuration from $DATABASE_URL

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.path.join(BASE_DIR, 'db.postgres'),
#         'USER': 'mpmmgyzacgaggy',
#         'PASSWORD': 'ezochPba5uMphirAwpORXZhR53',
#         'HOST': 'ec2-54-83-52-71.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }

import dj_database_url
DATABASE_URL = 'postgres://mvvyrwsojkwwmx:fntVrz8rGlcP7ofSIXlIHLGLNi@ec2-54-225-223-40.compute-1.amazonaws.com:5432/d3t664j51le0km'
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}
# DATABASES['default'] = dj_database_url.config()

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Melbourne'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static_in_pro', 'static_root')
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_DIRS = (
                    #os.path.join(BASE_DIR,'static_in_pro', 'our_static'),
                  )
# ------------- HEROKU STATIC ------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
print BASE_DIR
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'
#
# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static_in_env', 'media_root')



from .email_credentials import EMAIL_ADDRESS, EMAIL_PASSWORD
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = EMAIL_ADDRESS
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
EMAIL_PORT = 587
EMAIL_USE_TLS = True


CRISPY_TEMPLATE_PACK = 'bootstrap3'
