import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = [
    ("Ruidy", "ruidy.nemausat@gmail.com"),
    ("VillaFleurie", "location.villafleurie@gmail.com")
]

SECRET_KEY = os.environ.get('SECRET_KEY')

if os.environ.get('ENV') == 'PRODUCTION':
    DEBUG = False
    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': '5432',
            'ATOMIC_REQUESTS': True
        }
    }
    # PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    # STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
    # STATIC_TMP = os.path.join(PROJECT_ROOT, 'static')
    # # Extra places for collectstatic to find static files.
    # STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)
    # os.makedirs(STATIC_TMP, exist_ok=True)
    # os.makedirs(STATIC_ROOT, exist_ok=True)
    STATIC_ROOT = "/static_files/"
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    CONN_MAX_AGE = 500


else:
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            # 'NAME': 'villafleurie',
            # 'USER': 'nemausat',
            # 'PASSWORD': '',
            # 'HOST': '',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': '5432',
            'ATOMIC_REQUESTS': True
        }
    }
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "rental", "static", "rental"), ]
    # PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    # STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# STATIC_TMP = os.path.join(PROJECT_ROOT, 'static')
# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)
# os.makedirs(STATIC_TMP, exist_ok=True)
# os.makedirs(STATIC_ROOT, exist_ok=True)


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
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
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

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]


WSGI_APPLICATION = 'villafleurie.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'fr'
TIME_ZONE = 'America/Guadeloupe'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = "[VillaFleurieGuadeloupe] "
DEFAULT_FROM_EMAIL = "'Nilka, VillaFleurie' <location.villaFleurie@gmail.com>"
EMAIL_HOST_USER = "location.villafleurie@gmail.com"
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
