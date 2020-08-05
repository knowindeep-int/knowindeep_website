from django.contrib import admin


from .models import BlogTopics, Blog, Comment, Author
# from django.apps import apps

# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

class BlogTopicsInline(admin.TabularInline):
    model = BlogTopics
    fields = ['author_name','heading','youtube_link','no_of_likes','content']
    extra = 1
    readonly_fields = ['no_of_likes']

    
    
    
# class LikeInline(admin.StackedInline):
#     model = Like
#     extra = 1
#     max_num = 1

class BlogTopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['author_name','link_to','heading','youtube_link','no_of_likes','content']})
    ]
    readonly_fields = ['no_of_likes']
    inlines = []
    search_fields = ['heading','content']

class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['topic','topic_image','topic_content','no_of_views']}),
        ('Date information', {'fields': [], 'classes': ['collapse']})
    ]
    list_display = ['topic','topic_content','no_of_views']
    ordering = ['-no_of_views']
    readonly_fields = ['no_of_views']
    inlines = [BlogTopicsInline,]
    search_fields = ['topic','topic_content']





admin.site.register(BlogTopics, BlogTopicAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
# admin.site.register(Like)
admin.site.register(Author)