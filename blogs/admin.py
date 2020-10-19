from django.contrib import admin


from .models import BlogTopics, Project, Comment, Profile, Like
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
    fields = ['author','description','heading','youtube_link','content',]
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
        (None, {'fields':['author','link_to','heading','youtube_link','content','description']})
    ]
    inlines = [LikeInline,CommentInline]
    search_fields = ['heading','content']

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['title','image','overview','no_of_views','pre_req','isApproved']}),
        ('Date information', {'fields': [], 'classes': ['collapse']})
    ]
    list_display = ['title','overview','no_of_views']
    ordering = ['-no_of_views']
    readonly_fields = ['no_of_views']
    inlines = [BlogTopicsInline,]
    search_fields = ['title','overview']





admin.site.register(BlogTopics,BlogTopicAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Profile)