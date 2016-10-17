### WARNING!: do not keep this file in repository;
### create it from sample_env_setting.py every time on every new
### server and fill in proper settings for that new environment

### Do not modify next 2 lines
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w7kda3-mi2y4f8j$@gq6m_9ler3w+u5((^2r!hr*k#rl!osro('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost','127.0.0.1', 'students.vitaliykonchyts.com']

# website root url
PORTAL_URL = 'http://students.vitaliykonchyts.com'

DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'students_user1',
        'PASSWORD': '5282',
        'NAME': 'students_db1',
    }
}

# email settings
# please, set your smtp server details and your admin email
ADMIN_EMAIL = 'vitaliy.konchyts@gmail.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True 
EMAIL_USE_SSL = False

# static files
STATIC_URL = '/static/'
STATIC_ROOT = '/path/to/folder/with/static/files/'

# media files
MEDIA_URL = '/media/'
MEDIA_ROOT = '/path/to/folder/with/media/files/'

# facebook API Keys
SOCIAL_AUTH_FACEBOOK_KEY = '283971392002267'
SOCIAL_AUTH_FACEBOOK_SECRET = '35d91e466a666a6debe14ef6b728f926'

# admins
ADMINS = (('Vitaliy', 'vitaliy.konchyts@gmail.com'),)
MANAGERS = (('Manager', 'manager@gmail.com'),)