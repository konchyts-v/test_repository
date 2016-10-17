### WARNING!: do not keep this file in repository;
### create it from sample_env_setting.py every time on every new
### server and fill in proper settings for that new environment

### Do not modify next 2 lines
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

### You can modify below settings:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        #'USER': 'students_user1',
        #'PASSWORD': '5282',
        'USER': 'root',
        'PASSWORD': '5282',
        'NAME': 'students_db1',
        'TEST': {
        	'CHARSET': 'utf8',
        	'COLLATION': 'utf8_general_ci',
        },
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pzr%p&3jhs1035op4mf_u3c@8(6zakl495x=v*r^jg$&(x1h$2'

# website root url
PORTAL_URL = 'http://localhost:8000'

# email settings
ADMIN_EMAIL = ''
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# static and media resources
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

# facebook API Keys
SOCIAL_AUTH_FACEBOOK_KEY = '1766001193646823'
SOCIAL_AUTH_FACEBOOK_SECRET = '338856978c9bc6dceb2cb315e6ff14f5'