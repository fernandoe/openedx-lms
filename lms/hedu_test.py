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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'ATOMIC_REQUESTS': True,
    },
    'student_module_history': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}
