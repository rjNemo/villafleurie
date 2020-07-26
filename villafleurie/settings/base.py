import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rental.apps.RentalConfig'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware'
]

INTERNAL_IPS = ['127.0.0.1']
ROOT_URLCONF = 'villafleurie.urls'
WSGI_APPLICATION = 'villafleurie.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

# localisation, accessibility
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'America/Guadeloupe'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# static files
STATIC_URL = '/static/'
STATIC_ROOT = "/static_files/"

MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'

# Email settings
ADMINS = [
    ("Ruidy", "ruidy.nemausat@gmail.com"),
    ("VillaFleurie", "location.villafleurie@gmail.com")
]
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = "[VillaFleurieGuadeloupe] "
DEFAULT_FROM_EMAIL = "'Nilka, VillaFleurie' <location.villaFleurie@gmail.com>"
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

CELERY_BROKER_URL = "amqp://rabbitmq"
