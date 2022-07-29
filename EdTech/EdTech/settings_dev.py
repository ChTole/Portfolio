DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edtech',
        'USER': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'init_command': "SET sql_mode='STRICT_ALL_TABLES'",
    }
}

STATIC_ROOT = 'static/admin'