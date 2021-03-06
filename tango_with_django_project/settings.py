#coding: UTF-8
"""
Django settings for tango_with_django_project project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


from rango import keys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#931l#hlt@!kkp-z1u&(kzyn_z(i7ngf-=&85ex#z97vcf=3yf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rango',
    'registration',
    # 'registration_email',
    'bootstrap_toolkit',
    'DjangoUeditor',
    'bootstrap3',
    # 'captcha',
    # 'social_auth',
    # 'chartjs',
    # 'social_django',

    # 'raven.contrib.django.raven_compat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

ROOT_URLCONF = 'tango_with_django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.request",

                # 'social_django.context_processors.backends',  # <--
                # 'social_django.context_processors.login_redirect', # <--
            ],
        },
    },
]

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'


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

# TIME_ZONE = 'UTC'
# TIME_ZONE = 'Asia/Shanghai'
TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static1')
STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


# Auth
# LOGIN_URL = '/rango/login/'

# Session
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 60*60*24*30

# django-registration-redux
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.

SEND_ACTIVATION_EMAIL = False
REGISTRATION_EMAIL_SUBJECT_PREFIX = '^^'

# LOGIN_REDIRECT_URL = '/rango/'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/accounts/logout/'

# more settings see: http://django-registration-redux.readthedocs.org/en/latest/
# ---------------------------------------------------------

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'daya0576@gmail.com'
EMAIL_HOST_PASSWORD = keys.G_EMAIL_KEY
EMAIL_PORT = 587
# EMAIL_PORT = 25
EMAIL_USE_TLS = True
# ---------------------------------------------------------

#  Email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.qq.com'
# # EMAIL_HOST_USER = 'me@changchen.me'
# EMAIL_HOST_USER = '746058508@qq.com'
# EMAIL_HOST_PASSWORD = keys.ME_EMAIL_KEY
# EMAIL_PORT = 465
# # EMAIL_PORT = 25
# EMAIL_USE_TLS = True
# ---------------------------------------------------------

SITE_ID = 3

# baidu editor
TOOLBARS_SETTINGS = {
    "daya1":[[
            'fullscreen', 'source', '|', 'undo', 'redo',
            '|','bold', 'italic', 'underline', 'strikethrough', 'autotypeset',
            '|', 'forecolor', 'fontfamily', 'fontsize', 'backcolor', 'link',
            '|', 'insertorderedlist', 'insertunorderedlist',  'cleardoc',
            '|', 'simpleupload', 'insertimage', 'emotion', 'scrawl', 'insertvideo', 'music', 'attachment',
            '|', 'map', 'gmap',  'insertcode', 'template',
            '|','horizontal', 'date', 'time', 'spechars', 'snapscreen', '|']]
}

UEDITOR_SETTINGS={
    "config":{
        #这里放ueditor.config.js里面的配置项.......
        "toolbars" : [[
            'fullscreen', 'source', '|', 'undo', 'redo',
            '|','bold', 'italic', 'underline', 'strikethrough', 'autotypeset',
            '|', 'forecolor', 'fontfamily', 'fontsize', 'backcolor', 'link',
            '|', 'insertorderedlist', 'insertunorderedlist',  'cleardoc',
            '|', 'simpleupload', 'insertimage', 'emotion', 'scrawl', 'insertvideo', 'music', 'attachment',
            '|', 'map', 'gmap',  'insertcode', 'template',
            '|','horizontal', 'date', 'time', 'spechars', 'snapscreen', '|']],
        "enableAutoSave": "false"


    },
    "upload":{
        #这里放php/config.json里面的配置项.......
        "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".PNG", ".JPG", ".JPEG", ".GIF", ".BMP"]
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'rango.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

#  LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             # 'handlers': ['console'],
#             'level': 'DEBUG',
#         },
#     }

# }
