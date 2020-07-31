from django.contrib import admin

from .models import BlogTopics, Blog, Comment, Like
# from django.apps import apps

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

class BlogTopicsInline(admin.TabularInline):
    model = BlogTopics
    extra = 1
    
    
class LikeInline(admin.StackedInline):
    model = Like
    extra = 1
    max_num = 1

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['topic']}),
        ('Date information', {'fields': [], 'classes': ['collapse']})
    ]
    inlines = [BlogTopicsInline]

class BlogTopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['heading']})
    ]
    inlines = [LikeInline]

admin.site.register(BlogTopics)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
admin.site.register(Like)