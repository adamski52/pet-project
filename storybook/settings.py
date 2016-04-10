import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# sorry github ninjas - this gets regenned before it's real :(
SECRET_KEY = 'r7-$l0dtu_*on%((#s$lkbi^_-^469_!(33_5f-pp$x*#f#dez'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api'
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
    'localhost:8000',
    'jonathanadamski.com',
    'storybookkennels.com'
)

COLLAGE_MAX_RESULTS = 80
COLLAGE_ALLOWED_TYPES = ["jpg", "jpeg", "png"]
COLLAGE_WEB_THUMBNAIL_DIRECTORY = "images/collages/thumbnails/"
COLLAGE_WEB_FULL_DIRECTORY = "images/collages/full/"
COLLAGE_PENDING_DIRECTORY = "/Users/jon/Projects/storybook-client/images/collages/"
COLLAGE_FULL_DIRECTORY = COLLAGE_PENDING_DIRECTORY + "full/"
COLLAGE_THUMBNAIL_DIRECTORY = COLLAGE_PENDING_DIRECTORY + "thumbnails/"
COLLAGE_JUNK_DIRECTORY = COLLAGE_PENDING_DIRECTORY + "junk/"
COLLAGE_CROPPED_WIDTH = 100
COLLAGE_CROPPED_HEIGHT = 100

UPLOADED_FILES_USE_URL = False
FILE_UPLOAD_PERMISSIONS = 0o644
UPLOADED_FILES_ALLOWED_TYPES = ["text/plain", "application/pdf", "image/jpeg", "image/jpg", "image/png"]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.jonathanadamski.com'
EMAIL_HOST_USER = 'noreply@jonathanadamski.com'
EMAIL_HOST_PASSWORD = 'notreal'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ROOT_URLCONF = 'storybook.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/Users/jon/Projects/storybook/'],
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


WSGI_APPLICATION = 'storybook.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storybook',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


#JWT_AUTH = {
#    'JWT_ALLOW_REFRESH': True,
#    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1)
#}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#    '/Users/jon/Projects/storybook-client/',
#]
