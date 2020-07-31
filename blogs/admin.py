from django.contrib import admin

from .models import BlogTopics, Blog, Comment, Like
# from django.apps import apps

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

admin.site.register(BlogTopics)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Like)