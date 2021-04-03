from django.contrib import admin
from project.models import Blog,Topic,SubTopic

# Register your models here.
admin.site.register(Blog)
admin.site.register(Topic)
admin.site.register(SubTopic)