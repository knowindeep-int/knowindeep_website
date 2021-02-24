from .base import *
from dotenv import load_dotenv
load_dotenv()
DEBUG = True

SECRET_KEY = 'e(nyyh#nxx2o28m4$v9ttb4)5z$(_ba^0qgelbfygu&5z+mlp('

INSTALLED_APPS += [
   
]

ALLOWED_HOSTS = []

SITE_ID = 0

MIDDLEWARE += []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}