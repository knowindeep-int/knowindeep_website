from .base import *

DEBUG = True

SECRET_KEY = 'e(nyyh#nxx2o28m4$v9ttb4)5z$(_ba^0qgelbfygu&5z+mlp('

INSTALLED_APPS += [
   
]

SITE_ID = 0

MIDDLEWARE += []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}