"""
Django settings for track project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from .settings_secret import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['track.ap-northeast-2.elasticbeanstalk.com', 'localhost']


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	'static_precompiler',

	'accounts.apps.AccountsConfig',
	'feed.apps.FeedConfig'
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

ROOT_URLCONF = 'track.urls'

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

WSGI_APPLICATION = 'track.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if DEBUG:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}
else:
	if 'DEVINT_DB_MYSQL_HOST' in os.environ:
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.mysql', 
				'USER': os.environ['DEVINT_DB_MYSQL_USER'],
				'NAME': os.environ['DEVINT_DB_MYSQL_DB'],
				'PASSWORD': os.environ['DEVINT_DB_MYSQL_PASSWORD'],
				'HOST': os.environ['DEVINT_DB_MYSQL_HOST'],
				'PORT': '3306',
			}
		}
	else:
		DATABASES = {
			'default': {
				'ENGINE': 'django.db.backends.mysql', 
				'USER': os.environ['RDS_USERNAME'],
				'NAME': os.environ['RDS_DB_NAME'],
				'PASSWORD': os.environ['RDS_PASSWORD'],
				'HOST': os.environ['RDS_HOSTNAME'],
				'PORT': '3306',
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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_PRECOMPILER_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATIC_PRECOMPILER_COMPILERS = (
	('static_precompiler.compilers.LESS', {
		"executable": "/usr/local/bin/lessc",
	}),
)

LOGIN_URL = '/accounts/login'
LOGOUT_REDIRECT_URL = LOGIN_URL
