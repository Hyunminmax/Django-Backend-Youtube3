"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'password123')
DEBUG = bool(int(os.environ.get('DEBUG', 0))) # 0: False
ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition
DJANGO_SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
]
CUSTOM_USER_APPS = [
    "daphne",
    "users.apps.UsersConfig",  # Congif: label 변경할 일이 많다.
    "videos.apps.VideosConfig",
    "comments.apps.CommentsConfig",
    "subscriptions.apps.SubscriptionsConfig",
    "reactions.apps.ReactionsConfig",
    "rest_framework",
    "drf_spectacular",
    "channels",
    "chat.apps.ChatConfig",
]


INSTALLED_APPS = CUSTOM_USER_APPS + DJANGO_SYSTEM_APPS

# Channels를 사용하기 위한 설정
ASGI_APPLICATION = 'app.route.application' # Socket과 같은 (비동기처리) + HTTP(동기)

# 동기 vs 비동기
# 웹소켓 채팅을 구성했다 >> 웹소켓의 원리는 무엇인가?
# HTTP와 웹소켓의 차이점은 무엇인가?
# HTTP - 연결방식: http://
# SOCKET - 연결방식: ws://, Hand Shake 양방향 통신이 가능해진다, Low Overhade, Frame(웹소켓에서 데이터를 나누는 단위)
# STREAMING - 영상 파일은 어떻게 보낼건가? TCP/UDP, 3 ways handshake


# FAST API = 비동기 + 동기
WSGI_APPLICATION = "app.wsgi.application" # HTTP를 base로하는 REST API와 같은 동기 처리

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]




# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.environ.get("DB_HOST"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASS"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django의 Cusom UserModel - 기존 장고의 유저 인증 기능을 가져온다.
AUTH_USER_MODEL = "users.User"

REST_FRAMEWORK = {
    # YOUR SETTINGS
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema"
}

CHANNEL_LAYERS = {
    "default":{
        "BACKEND":"channels.layers.InMemoryChannelLayer"
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'