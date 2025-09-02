"""
Django settings for LiquidRound project.

Updated for Django 5.1.x with modern best practices.
"""

import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
WEBSITE_ROOT = BASE_DIR.parent
PROJECT_ROOT = WEBSITE_ROOT.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='w0&++iu9-n-bh0ddu2*wuq7*u$$qt0bp$i)t%4x5%v5lf)h4l=')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0', '*']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third party apps
    'corsheaders',
    'pipeline',
    'imagekit',
    
    # Local apps
    'accounts',
    'statpages',
    'companies',
    'listings',
    'admindeck',
    'msgs',
    'news',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

AUTHENTICATION_BACKENDS = [
    'accounts.auth_backend.TokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            WEBSITE_ROOT / 'templates' / 'admindeck',
            WEBSITE_ROOT / 'templates' / 'listings',
            WEBSITE_ROOT / 'templates',
        ],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database - Updated to use SQLite by default
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_ROOT / 'staticfiles'

STATICFILES_DIRS = [
    WEBSITE_ROOT / 'core' / 'static',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder',
]

# Use WhiteNoise for static file serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_ROOT / 'media'

# Pipeline settings (simplified)
PIPELINE = {
    'PIPELINE_ENABLED': not DEBUG,
    'STYLESHEETS': {
        'styles': {
            'source_filenames': (
                'css/tailwind.css',
                'css/liquidround.css',
                'css/plugins/bootstrap/css/bootstrap.min.css',
                'css/style.css',
                'css/header-default.css',
                'css/footer-v3.css',
                'css/plugins/animate.css',
                'css/plugins/line-icons/line-icons.css',
                'css/plugins/font-awesome/css/font-awesome.min.css',
                'css/plugins/image-hover/css/img-hover.css',
                'css/theme-colors/default.css',
                'css/theme-skins/dark.css',
                'css/main.css',
            ),
            'output_filename': 'css/styles.css',
        },
    },
    'JAVASCRIPT': {
        'scripts_bottom': {
            'source_filenames': (
                'js/jquery/jquery.min.js',
                'js/jquery/jquery-migrate.min.js',
                'js/bootstrap/js/bootstrap.min.js',
                'js/back-to-top.js',
                'js/smoothScroll.js',
                'js/jquery.parallax.js',
                'js/image-hover/js/touch.js',
                'js/image-hover/js/modernizr.js',
                'js/jquery.mockjax.js',
                'js/jquery.autocomplete.min.js',
                'js/jquery.jscroll.min.js',
                'js/hogan.min.js',
                'js/templates.js',
                'js/app.js',
                'js/main.js',
            ),
            'output_filename': 'js/scripts_bottom.js',
        }
    }
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

