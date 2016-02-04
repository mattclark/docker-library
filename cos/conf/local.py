import os

SECRET_KEY = 'ChangeMe!'
NEVERCACHE_KEY = 'ChangeMe!!'

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'staging.cos.io',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/data/cos_staging.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

CACHE_MIDDLEWARE_SECONDS = 60

CACHE_MIDDLEWARE_KEY_PREFIX = 'testing'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'