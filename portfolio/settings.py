from pathlib import Path
from decouple import config
import dj_database_url
from dotenv import load_dotenv 
import os


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1,portfolio-website-1-yc1b.onrender.com').split(',')


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

LOGIN_URL = '/dashboard/login/'
LOGOUT_URL = '/dashboard/logout/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'info',
    'dashboard',
    'cloudinary_storage',
    'cloudinary',
    'ckeditor',
    'rest_framework',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                'filter_tags': 'info.templatetags.filter',
            }
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

# if not DEBUG:
#     # Database
#     # DATABASES = {
#     #     'default': dj_database_url.config(
#     #         default=config('DATABASE_URL', default='mysql://root:Hacs!1tack@127.0.0.1:3306/mysql')
#     #     )
#     # }
#     # Storage settings
#     CLOUDINARY_STORAGE = {
#         'CLOUD_NAME': config('CLOUD_NAME', default=''),
#         'API_KEY': config('API_KEY', default=''),
#         'API_SECRET': config('API_SECRET', default=''),
#     }
#     DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
#     DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# else:
#     DATABASES = {
#         'default': dj_database_url.config(
#             default='mysql://root:Hacs!1tack@127.0.0.1:3306/mysql'
#         )
#     }

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# if not DEBUG:
#     # Database
#     # https://docs.djangoproject.com/en/2.2/ref/settings/#databases
#     DATABASES = {
#         'default': dj_database_url.config(
#             default=config('DATABASE_URL')
#         )
#     }
    
#     # Storage settings
#     CLOUDINARY_STORAGE = {
#         'CLOUD_NAME': config('CLOUD_NAME', default=''),
#         'API_KEY': config('API_KEY', default=''),
#         'API_SECRET': config('API_SECRET', default=''),
#     }
#     DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
#     DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


    # DATABASES = {
    #     'default': {
    #         # 'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #         'ENGINE': 'django.db.backends.mysql',
    #         'USER': 'root',
    #         'PASSWORD': 'Hacs!1tack',
    #         'HOST': '127.0.0.1',
    #         'PORT': '3306'
    #     }
    # }

#     DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL', default='mysql://mhacs:Hacs!1tack@127.0.0.1:3306/mysql')
#     )
# }


# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')




# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'portfolio/static/'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
