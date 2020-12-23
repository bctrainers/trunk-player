import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCAL_SETTINGS = True
DEBUG = False

ALLOWED_HOSTS = ['*']
#ALLOW_ANONYMOUS = True

# Make this unique, and don't share it with anybody.
# You can use http://www.miniwebtool.com/django-secret-key-generator/ to create one.
SECRET_KEY = 'YouNeedToSetAReallySecureKeyHereViaTheLinkAbove'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
CSRF_TRUSTED_ORIGINS = ["yourdomain.tld"]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
USE_X_FORWARDED_HOST = False

# Site globals and email
TIME_ZONE = 'America/Chicago'
SITE_TITLE = 'YourDomain.tld'
SITE_EMAIL = 'admin@YourDomain.tld'
DEFAULT_FROM_EMAIL='YourDomain <admin@yourdomain.tld>'
SERVER_EMAIL='admin@yourdomain.tld'
ADMINS=[('Username1', 'admin@yourdomain.com'), ('Username2', 'someone@sometld.acme')]

# Set to logical directories...
AUDIO_URL_BASE = '/audio_files/'
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

# Allow TalkGroup access restrictions
ACCESS_TG_RESTRICT = False

# Allow Some Editing
SHOW_PROFILE_LINK = True
ENABLE_USER_SCAN_LISTS = True
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2500
SEND_ADMIN_EMAIL_ON_UNIT_NAME = True


#
# This is for your caches. If you do not configure your redis caches correctly, you WILL have a very slow site.
#                                                                                 And you will have a bad time.
# 
# Your Redis Server URL has to be in the form of the following:
#
#    Mode to connect as:        redis://
#        Sorta need this, otherwise it wont work!
#
#    IP to connect TO:          192.168.20.206
#       This can be localhost, 127.0.0.1, some LAN IP... or heavens forbid, a WAN IP.
#
#    PORT to connect ON:        6379
#        Default is 6379.
#
#    Database Keyspace to use:  /8 /9 /10
#       Leaving the keyspace blank will make it use DB 0, and isn't ideal. 
#       For me, I have multiuple uses for my Redis cluster - so TrunkPlayer was assigned 8 9 and 10.
#

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://192.168.20.206:6379/9')],
                "channel_capacity": {
                    "http.request": 200,
                    "http.response!*": 10,
                    "websocket.send*": 20,
            },
            "capacity": 100,
        },
        "ROUTING": "radio.routing.channel_routing",
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.20.206:6379/10",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
    "select2": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.20.206:6379/8",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}
SELECT2_CACHE_BACKEND = "select2"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trunk_player',
        'USER': 'trunk_player_user',
        'PASSWORD': 'YouNeedToSetAReallySecurePasswordHere',
        'HOST': '192.168.20.201',
        'PORT': '',
    }
}
