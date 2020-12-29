from django.utils.text import slugify
import random
import string

from . import models

DONT_USE = ['create','user','login','register','remove','approve',]

def random_string_generator(size=10,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance,new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        if instance.__class__ == models.Project:
            slug = slugify(instance.title)
        elif instance.__class__ == models.Chapter:
            slug = slugify(instance.heading)
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
