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

# MODULESTORE = {
#     "default": {
#         "ENGINE": "xmodule.modulestore.mixed.MixedModuleStore",
#         "OPTIONS": {
#             "mappings": {},
#             "stores": [
#                 {
#                     "NAME": "draft",
#                     "DOC_STORE_CONFIG": {
#                         "collection": "modulestore",
#                         "db": "test",
#                         "host": [
#                             os.environ.get('MONGODB_MONGODB_SERVICE_HOST')
#                         ],
#                         "port": 27017
#                     },
#                     "ENGINE": "xmodule.modulestore.mongo.DraftMongoModuleStore",
#                     "OPTIONS": {
#                         "collection": "modulestore",
#                         "db": "test",
#                         "default_class": "xmodule.hidden_module.HiddenDescriptor",
#                         "fs_root": "** OVERRIDDEN **",
#                         "host": [
#                             os.environ.get('MONGODB_MONGODB_SERVICE_HOST')
#                         ],
#                         "port": 27017,
#                         "render_template": "edxmako.shortcuts.render_to_string"
#                     }
#                 },
#                 {
#                     "NAME": "xml",
#                     "ENGINE": "xmodule.modulestore.xml.XMLModuleStore",
#                     "OPTIONS": {
#                         "data_dir": "** OVERRIDDEN **",
#                         "default_class": "xmodule.hidden_module.HiddenDescriptor"
#                     }
#                 }
#             ]
#         }
#     }
# }
#
# CONTENTSTORE = {
#     "DOC_STORE_CONFIG": {
#         "collection": "modulestore",
#         "db": "test",
#         "host": [
#             os.environ.get('MONGODB_MONGODB_SERVICE_HOST')
#         ],
#         "port": 27017
#     },
#     "ENGINE": "xmodule.contentstore.mongo.MongoContentStore",
#     "OPTIONS": {
#         "db": "test",
#         "host": [
#             os.environ.get('MONGODB_MONGODB_SERVICE_HOST')
#         ],
#         "port": 27017
#     }
# }

MODULESTORE = {
    u'default': {
        u'ENGINE': u'xmodule.modulestore.mixed.MixedModuleStore',
        u'OPTIONS': {
            u'stores': [{
                u'ENGINE': u'xmodule.modulestore.split_mongo.split_draft.DraftVersioningModuleStore',
                u'DOC_STORE_CONFIG': {
                    u'replicaSet': u'',
                    u'connectTimeoutMS': 2000,
                    u'socketTimeoutMS': 3000,
                    u'db': u'edxapp',
                    u'collection': u'modulestore',
                    u'ssl': False,
                    u'host': [os.environ.get('MONGODB_MONGODB_SERVICE_HOST')],
                    u'user': u'edxapp',
                    u'read_preference': u'PRIMARY',
                    u'password': u'password',
                    u'port': 27017
                },
                u'NAME': u'split',
                u'OPTIONS': {
                    u'fs_root': u'/edx/var/edxapp/data',
                    u'render_template': u'edxmako.shortcuts.render_to_string',
                    u'default_class': u'xmodule.hidden_module.HiddenDescriptor'
                }
            }, {
                u'ENGINE': u'xmodule.modulestore.mongo.DraftMongoModuleStore',
                u'DOC_STORE_CONFIG': {
                    u'replicaSet': u'',
                    u'connectTimeoutMS': 2000,
                    u'socketTimeoutMS': 3000,
                    u'db': u'edxapp',
                    u'collection': u'modulestore',
                    u'ssl': False,
                    u'host': [os.environ.get('MONGODB_MONGODB_SERVICE_HOST')],
                    u'user': u'edxapp',
                    u'read_preference': u'PRIMARY',
                    u'password': u'password',
                    u'port': 27017
                },
                u'NAME': u'draft',
                u'OPTIONS': {
                    u'fs_root': u'/edx/var/edxapp/data',
                    u'render_template': u'edxmako.shortcuts.render_to_string',
                    u'default_class': u'xmodule.hidden_module.HiddenDescriptor'
                }
            }
            ], u'mappings': {}
        }
    }
}

CONTENTSTORE = {
    u'ENGINE': u'xmodule.contentstore.mongo.MongoContentStore',
    u'DOC_STORE_CONFIG': {
        u'replicaSet': u'',
        u'connectTimeoutMS': 2000,
        u'socketTimeoutMS': 3000,
        u'db': u'edxapp',
        u'collection': u'modulestore',
        u'ssl': False,
        u'host': [os.environ.get('MONGODB_MONGODB_SERVICE_HOST')],
        u'user': u'edxapp',
        u'read_preference': u'PRIMARY',
        u'password': u'password', u'port': 27017
    },
    u'ADDITIONAL_OPTIONS': {},
    u'OPTIONS': {
        u'db': u'edxapp',
        u'ssl': False,
        u'host': [os.environ.get('MONGODB_MONGODB_SERVICE_HOST')],
        u'user': u'edxapp',
        u'password': u'password',
        u'port': 27017
    }
}
