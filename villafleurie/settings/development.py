""" Settings to be used in development """

import os

from .base import *

SECRET_KEY = "not_so_secret_key"
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'villafleurie',
        'USER': 'nemausat',
        'PASSWORD': '',
        'HOST': '',
        # 'NAME': 'postgres',
        # 'USER': 'postgres',
        # 'HOST': 'db',
        # 'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}
STATICFILES_DIRS = [os.path.join(BASE_DIR, "rental", "static", "rental"), ]

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
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
