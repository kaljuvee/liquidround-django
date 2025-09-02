from .base import *

# Override settings for local development
DEBUG = True

# Database for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Disable pipeline for development
PIPELINE['PIPELINE_ENABLED'] = False

# Allow all hosts for local development
ALLOWED_HOSTS = ['*']

# Email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'