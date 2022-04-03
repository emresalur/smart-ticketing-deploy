"""
Django settings for ticketing project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import pymysql

pymysql.install_as_MySQLdb()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(^56-gyqopdo1+ngy(5+p++d0ad*nk8!sq#b&q5+8&2ye#guf)'

USER_KEY = 'SECURITYHSGU'

NOW_HOST = "http://127.0.0.1:8000/"
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'smart'
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

ROOT_URLCONF = 'ticketing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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

WSGI_APPLICATION = 'ticketing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
  # test database
        'TEST': {
            'CHARSET':'utf8',
            'NAME': 'test',  # A database named test will be generated during the test, and Django will automatically delete the database after the test is over
        }
    }
}
# DATABASES = {
#
#     'default': {
#          'ENGINE': 'django.db.backends.mysql',
#          #database name
#          'NAME': 'study',
#          'USER': 'root',
#          'PASSWORD': '123456',
#          'HOST': '127.0.0.1',
#          'PORT': '3306',
#          'OPTIONS': {
#             'autocommit': True,
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_DIRS = (
    os.path.join(BASE_DIR, 'static')
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# adress for img 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.UserProfile'
LOGIN_URL = '/accounts/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/accounts/logout'


#mail config
EMAIL_HOST = 'smtp.163.com'
# number port
EMAIL_PORT = 25
#email address
EMAIL_HOST_USER = '15010226955@163.com'
# set sender authorization code
EMAIL_HOST_PASSWORD = 'PWTYOXQEQWFQYSMO'
# Set whether to enable safe links
EMAIL_USER_TLS = True
