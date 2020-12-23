"""
Django settings for trunk_player project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGIN_URL = '/login/'
# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'local_override',
    'radio.apps.RadioConfig',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.instagram',
    'rest_framework',
    'channels',
    'pinax.stripe',
    'django_select2',
    'ckeditor',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'radio.custom_middleware.ExtendUserSession',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trunk_player.urls'

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
WSGI_APPLICATION = 'trunk_player.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# 'X-Forwarded-Proto' header for request.is_secure()
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
STATIC_URL = '/static/'
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "audio_files"),
#]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# NOTE: Setting `PAGE_SIZE` value will change how many items are shown per-page. 
#         Higher the setting, more DB i/o and more web bandwidth!
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'PAGINATE_BY': 50,                 # Default to 10
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100             # Maximum limit allowed when using `?page_size=xxx`.
}
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "audio_files")

# How far back an anonymous/guest users can see back in minutes
# 0 will disable the limit. Sane limit is between 1 and 30.
ANONYMOUS_TIME = 5 
# This Agency must exist in radio.Agency
RADIO_DEFAULT_UNIT_AGENCY = 0
SITE_ID = 1
SOCIALACCOUNT_PROVIDERS = { 'google': { 'SCOPE': ['profile', 'email'], 'AUTH_PARAMS': { 'access_type': 'online' } } }
ACCOUNT_AUTHENTICATION_METHOD="username_email"
ACCOUNT_EMAIL_REQUIRED=True
LOGIN_REDIRECT_URL="/"

# AMAZON, GOOGLE, TWITTER, AND PINAX ARE UNUSED VARIABLES HERE.
AMAZON_ADDS = False
AMAZON_AD_TRACKING_ID = 'some-tracking-id-here'
AMAZON_AD_LINK_ID = 'some-hash-here'
AMAZON_AD_EMPHASIZE_CATEGORIES = 'some,ids,here'
AMAZON_AD_FALL_BACK_SEARCH = ['common', 'keywords', 'here',]
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-87256556-1'
ALLOW_GOOGLE_SIGNIN = False
TWITTER_ACTIVE = False
TWITTER_LIST_URL = None
#This is set (read:overridden) on settings_local.py
SITE_TITLE = 'Trunk-Player'
SITE_EMAIL = 'help@example.com'
PINAX_STRIPE_SECRET_KEY = '0'
PINAX_STRIPE_PUBLIC_KEY = '0'
PINAX_STRIPE_SECRET_KEY = 'sk_test_xxxxxxxxxxxxxxxxxxxx'
PINAX_STRIPE_PUBLIC_KEY = 'pk_test_xxxxxxxxxxxxxxxxxxxx'
PINAX_STRIPE_INVOICE_FROM_EMAIL = 'help@example.com'

# Which settings are passed into the javascript object js_config
JS_SETTINGS = ['SITE_TITLE', 'AUDIO_URL_BASE']

# Which settings are aviable to the template tag GET_SETTING
VISABLE_SETTINGS = ['SITE_TITLE', 'AUDIO_URL_BASE', 'CDN_URL_BASE', 'GOOGLE_ANALYTICS_PROPERTY_ID', 'COLOR_CSS', 'SITE_EMAIL', 'PINAX_STRIPE_PUBLIC_KEY', 'SHOW_STRIPE_PLANS', 'OPEN_SITE']

ALLOW_ANONYMOUS = True
ADD_TRANS_AUTH_TOKEN = '7cf5857c61284' # Token to allow adding transmissions

OPEN_SITE = True # If False new users cannot sign up
FIX_AUDIO_NAME = False

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'width': '100%',
    },
}
CKEDITOR_BASEPATH = "/static/ckeditor/"

# Load our local settings 
try:
    LOCAL_SETTINGS
except NameError:
    try:
        from trunk_player.settings_local import *
    except ImportError:
        print("Failed to open settings_local.py")
