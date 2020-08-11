from django.contrib import admin


from .models import BlogTopics, Blog, Comment, Author, Like
# from django.apps import apps

# models = apps.get_models()
                                                        # This can be used to register all models in the app
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

class BlogTopicsInline(admin.StackedInline):
    model = BlogTopics
    fields = ['author_name','description','heading','youtube_link','content',]
    extra = 1

    
    
    
class LikeInline(admin.StackedInline):
    model = Like
    extra = 0
    # max_num = 1

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    fields = ['link_to','timestamp','comment_text','user']
    readonly_fields = ['timestamp']

class BlogTopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['author_name','link_to','heading','youtube_link','content','description']})
    ]
    inlines = [LikeInline,CommentInline]
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





admin.site.register(BlogTopics,BlogTopicAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Author)