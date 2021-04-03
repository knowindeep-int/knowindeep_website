from django.contrib import admin


from .models import Chapter, Project, Comment, Profile, Like, Language, Package, Progress, Suggestion
# from django.apps import apps

# models = apps.get_models()
# This can be used to register all models in the app
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

class ChapterTopicsInline(admin.StackedInline):
    model = Chapter
    fields = ['author','content','title']
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

class ChapterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['author','link_to','content','slug','title','bookmark',]})
    ]
    search_fields = ['content']

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['title','image','overview', 'description', 'no_of_views','pre_req','isApproved', 'languages', 'difficulty_level', 'isCompleted', 'author','date_approved','bookmark',]}),
        ('Date information', {'fields': [], 'classes': ['collapse']})
    ]
    list_display = ['title','overview','no_of_views']
    ordering = ['-no_of_views']
    readonly_fields = ['no_of_views','isApproved']
    inlines = [ChapterTopicsInline, LikeInline,CommentInline]
    search_fields = ['title','overview']

# class BlogAdmin(admin.ModelAdmin):
#     fieldsets = [
#         'author', 'content', 'title','date_created','description','isApproved'
#     ]
#     list_display = ['title','description']
#     ordering = ['-date_created']
#     readonly_fields = ['date_created','isApproved']
#     search_fields = ['title','date_created']





admin.site.register(Chapter,ChapterAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Language)
admin.site.register(Package)
admin.site.register(Progress)
# admin.site.register(Blog)
admin.site.register(Suggestion)