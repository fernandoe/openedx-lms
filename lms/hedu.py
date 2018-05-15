from .devstack_docker import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ.get('EDXAPP_MYSQL_HOST'),
        "NAME": os.environ.get('EDXAPP_MYSQL_DB_NAME'),
        "USER": os.environ.get('EDXAPP_MYSQL_USER'),
        "PASSWORD": os.environ.get('EDXAPP_MYSQL_PASSWORD'),
        "PORT": "3306",
    }
}

CACHES = {
    "celery": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "integration_celery",
        "LOCATION": [
            os.environ.get('EDXAPP_MEMCACHED_HOST')
        ]
    },
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "sandbox_default",
        "LOCATION": [
            os.environ.get('EDXAPP_MEMCACHED_HOST')
        ]
    },
    "general": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "sandbox_general",
        "LOCATION": [
            os.environ.get('EDXAPP_MEMCACHED_HOST')
        ]
    },
    "mongo_metadata_inheritance": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "integration_mongo_metadata_inheritance",
        "LOCATION": [
            os.environ.get('EDXAPP_MEMCACHED_HOST')
        ]
    },
    "staticfiles": {
        "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
        "KEY_FUNCTION": "util.memcache.safe_key",
        "KEY_PREFIX": "integration_static_files",
        "LOCATION": [
            os.environ.get('EDXAPP_MEMCACHED_HOST')
        ]
    }
}
