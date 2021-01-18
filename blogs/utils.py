from django.utils.text import slugify
import random
import string
from dotenv import load_dotenv
load_dotenv()
from django.conf import settings
import os
from . import models

DONT_USE = ['remove','approve','admin','teach',]

def random_string_generator(size=10,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        if instance.__class__ == models.Project:
            slug = slugify(instance.title)
        elif instance.__class__ == models.Chapter:
            slug = slugify(instance.link_to.title)
            print(slug)
    if slug in DONT_USE:
        new_slug = slug + random_string_generator(size=4)
        return unique_slug_generator(instance,new_slug=new_slug)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(slug=slug,randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def save_user(backend, user, response, *args, **kwargs):

    try:
        profile = models.Profile.objects.get(user=user)
    except models.Profile.DoesNotExist:
        profile = models.Profile(
            dp = response['picture'],
            user=user
        )
        profile.save()

def getApiKey():
    if settings.DEBUG:
        UNSPLASH_API_KEY = os.getenv('UNSPLASH_API_KEY_DEBUG')
        PEXELS_API_KEY = os.getenv('PEXELS_API_KEY_DEBUG')
        IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID_DEBUG')
        IMGUR_BEARER = os.getenv('IMGUR_BEARER_DEBUG')
        return UNSPLASH_API_KEY,PEXELS_API_KEY,IMGUR_CLIENT_ID,IMGUR_BEARER
    else:
        UNSPLASH_API_KEY = os.getenv('UNSPLASH_API_KEY')
        PEXELS_API_KEY = os.getenv('PEXELS_API_KEY')
        IMGUR_CLIENT_ID = os.getenv('IMGUR_CLIENT_ID')
        IMGUR_BEARER = os.getenv('IMGUR_BEARER')
        return UNSPLASH_API_KEY,PEXELS_API_KEY,IMGUR_CLIENT_ID,IMGUR_BEARER