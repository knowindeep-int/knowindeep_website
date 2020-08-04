from django.contrib import admin

from .models import BlogTopics, Blog, Comment, Like, Author
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

class BlogTopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['heading','link_to','youtube_link']})
    ]
    inlines = []

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['topic','topic_image','topic_content']}),
        ('Date information', {'fields': [], 'classes': ['collapse']})
    ]
    inlines = [BlogTopicsInline,]





admin.site.register(BlogTopics, BlogTopicAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Author)