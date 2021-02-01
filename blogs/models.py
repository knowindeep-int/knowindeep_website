from django.db import models
from django.db.models.fields import TextField
from tinymce.models import HTMLField
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, int_list_validator, MaxValueValidator
from django.db.models import Max, Min
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings
import os
from knowindeep import Constants


class Language(models.Model):
    is_available = models.BooleanField(null = True, blank = True)
    name = models.CharField(max_length = 100,unique = True, primary_key = True)
    image = models.ImageField(blank = True,null= True, upload_to = 'languages/')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural  = "Languages"

    @classmethod
    def getAllLanguages(cls):
        languages = cls.objects.all()
        return languages
        
    @classmethod
    def getLanguageSearches(cls,search_input):
        language_searches = cls.objects.filter(name__icontains = search_input)
        return language_searches

class Profile(models.Model):
    account_number = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=200, null = True, blank = True)
    dp = models.ImageField(null=True,upload_to='profiles/', blank = True)
    github_id = models.URLField(max_length=70,null=True,blank=True)
    isAuthor = models.BooleanField(default=False)
    linkedin_id = models.URLField(max_length=70,null=True,blank=True)
    phone_number = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    skills = models.ManyToManyField(to = Language, related_name="skills", blank = True)
    total_earnings = models.IntegerField(null=True, blank=True)
    twitter_id = models.URLField(max_length=70, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #email_id = models.EmailField(max_length=30, unique=True, primary_key=True)
    #projects = models.ManyToManyField(to = 'Project', null = True, blank = True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

    @classmethod
    def getAuthorSearches(cls, search_input):
        author_searches = cls.objects.filter(
            Q(user__username__icontains = search_input)
        )
        return author_searches
    
    @classmethod
    def getProfile(cls,user):
        return cls.objects.get(user=user)

    #not used
    @classmethod
    def getUser(cls, name):
        profile = cls(name = name)
        return profile.user


    @property
    def getOngoingAndCompletedProjects(self):
        projects = self.projects.all()
        ongoing_projects = projects.filter(isCompleted=False)
        completed_projects = projects.filter(isCompleted=True)
        return ongoing_projects, completed_projects

    @property
    def getPackageProgressTuple(self):
        packages = self.packages.all()
        percent_progress = []
        
        for i in range(packages.count()):
            percent_progress.append(packages[i].progress.all().count() / packages[i].project.chapters.all().count() * 100)        
        
        return tuple(zip(packages, percent_progress))
    
    @property
    def skills_set(self):
        return self.skills.all()
    

    def is_verified(self, user):
        return user == self.user


class Blog(models.Model):
    author = models.ForeignKey(to =Profile, on_delete = models.CASCADE)
    content = RichTextUploadingField(blank=True,null=True)
    date_approved = models.DateTimeField(default = None, blank =True ,null=True) 
    description = models.TextField(blank=True,null=True)
    isApproved = models.BooleanField(default=False)
    title = models.CharField(max_length = 25, null =False, blank= False)

    def save(self, *args, **kwargs):
        if self.isApproved and self.date_approved is None:
            self.date_approved = timezone.now()
        elif not self.isApprove and self.date_approved is not None:
            self.date_approved = None
        super(Blog,self).save(*args,*kwargs)
    

# class PreRequisite(models.Model):
#     name = models.CharField(max_length = 100)

#     def __str__(self):
#         return self.name
    
#     class Meta:
#         verbose_name_plural = "Pre-Requisites"
    
#     @classmethod
#     def getAllPreReqs(cls):
#         pre_reqs = cls.objects.all()
#         return pre_reqs

#     @classmethod
#     def getPrereqSearches(cls,search_input):
#         prereq_searches = cls.objects.filter(name__icontains = search_input)
#         return prereq_searches


class Project(models.Model):
     # topic = models.CharField(max_length=30)
    # topic_image = models.ImageField(null=True, upload_to='media/')
    # topic_content = models.CharField(max_length=300, blank=True, null=True)
    author = models.ForeignKey(to = Profile, on_delete = models.CASCADE, related_name = "projects")
    date_approved = models.DateTimeField(default = None, blank =True ,null=True)  
    description = models.TextField(null = True, blank = True)
    difficulty_level = models.CharField(max_length = 100,null = True, blank = True, choices = ((Constants.EASY, Constants.EASY),(Constants.MEDIUM, Constants.MEDIUM), (Constants.HARD, Constants.HARD)))
    image = models.URLField(max_length=200,blank=True,null=True)
    isApproved = models.BooleanField(default=False)
    isCompleted = models.BooleanField(default = False) 
    languages = models.ManyToManyField(to = Language, blank = True)
    no_of_hours = models.DecimalField(null = True, blank = True, decimal_places = 1, max_digits = 4)
    no_of_views = models.IntegerField(default=0)
    no_of_likes = models.IntegerField(default=0)
    overview = models.CharField(max_length=300, null = True, blank = True)
    pre_req = models.CharField(max_length=300,null= True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    title = models.CharField(max_length=25)  
    
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.isApproved and self.date_approved is None:
            self.date_approved = timezone.now()
        elif not self.isApproved and self.date_approved is not None:
            self.date_approved = None
        super(Project,self).save(*args,*kwargs)
    
    @property
    def complete_project(self):
        self.isCompleted = True
        self.save()

    @property
    def get_absolute_url(self): 
        return reverse('blogs:sub_topic', kwargs={'slug': self.slug})

    @property
    def approveProject(self):
        self.isApproved = True
        # self.date_approved = timezone.now()
        self.save()

    @property
    def getCompleteUrl(self):
        if settings.DEBUG:
            return "http://%s%s" % ('127.0.0.1:8000' ,self.get_absolute_url)
        else:
            return "https://%s%s" % ('127.0.0.1:8000' ,self.get_absolute_url)

    @property
    def increase_view(self):
        if self.isCompleted:
            self.no_of_views += 1
            self.save()
        else:
            self.DoesNotExist = 0
            self.save()


    @classmethod
    def getAllChapters(cls, slug):
        project = cls.objects.get(slug = slug)
        return project.chapters.all()

    @classmethod
    def get_all_projects(cls):
        return cls.objects.filter(isCompleted = True)
    
    @classmethod
    def get_all_approved_projects(cls):
        return cls.objects.filter(isApproved = True, isCompleted = True)

    @classmethod
    def get_popular_approved_completed_projects(KClass):
        return KClass.objects.filter(isApproved = True, isCompleted = True).order_by('-no_of_views')[:5]

    @classmethod
    def get_popular_projects(KClass):
        return KClass.objects.filter(isCompleted = True).order_by('-no_of_views')[:5]
    
    @classmethod
    def getProjectSearches(cls, search_input):
        project_searches = cls.objects.filter(
            Q(slug__istartswith = search_input) |
            Q(title__icontains = search_input) |
            Q(author__user__username__icontains = search_input)
        )
        return project_searches

    @classmethod
    def get_project(cls, pk):
        return cls.objects.get(pk = pk)

    @classmethod
    def get_status(cls, pk):
        project = cls.objects.get(pk=pk)
        if project.title == None or project.title == "":
            return "title"
        if project.description == None or project.description == "":
            return "description"
        if project.difficulty_level == None or project.difficulty_level == "":
            return "difficulty_level"
        if project.overview == None or project.overview == "":
            return "overview"
        if project.image == None or project.image == "":
            return "image"
        if project.no_of_hours == None or project.no_of_hours == "":
            return "no_of_hours"
        if project.chapters.all().count() == 0 :
            return "chapter"
        return None

    @classmethod
    def getTitle(cls, slug):
        project = cls.objects.get(slug = slug)
        return project.title

    
    def canUserView(self, user):
        return self.isApproved or user.is_superuser


    @classmethod
    def getAllComments(cls, project_content_slug):
        chapter = cls.objects.get(slug = project_content_slug)
        return chapter.project_comments.all().order_by('-timestamp')
    
    def comments(self):
        return self.project_comments.all()

    def decreaseLikes(self):
        self.no_of_likes -= 1
        self.save()

    def has_user_liked(self,user):
        if not user.is_anonymous:
            try:
                #isLiked = Like.objects.get(profile__user__email=user.email,link_to=self)
                isLiked = self.likes.all().get(profile__user__email = user.email)
                # self.likes.get(profile.email_id == user.email)
                return True
            except Like.DoesNotExist:
                has_liked = False
                return False
        else:
            return None

    def increaseLikes(self):
        self.no_of_likes += 1
        self.save()
    
    def get_comment_url(self):
        return reverse("api:comment-post")

    def get_like_url(self):
        return reverse("api:like-post")

    @classmethod
    def getProject(cls, slug):
        project = cls.objects.get(slug = slug)
        return project
    
    @property
    def like_count(self):
        return self.likes.all().count()
        
class Chapter(models.Model):
    author = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, blank=True)
    content = RichTextUploadingField(blank=True,null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    link_to = models.ForeignKey(Project,on_delete=models.CASCADE, related_name="chapters")
    slug = models.SlugField(null=True,blank=True)
    title = models.CharField(max_length=30,null=True,blank=True)
   # content = models.CharField(max_length=1000, null=False,blank=False)
  #  content = HTMLField()  .
    # no_of_likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Chapters"
        
    def __str__(self):
        # return self.link_to.title
        return self.content[:10]
    
    @property
    def get_absolute_url(self): 
        return reverse('blogs:chapter_post', kwargs={'slug': self.link_to.slug, 'chapter': self.slug})

   
    
    @property
    def getCompleteUrl(self):
        if settings.DEBUG:
            return "http://%s%s" % ('127.0.0.1:8000' ,self.get_absolute_url)
        else:
            return "https://%s%s" % ('127.0.0.1:8000' ,self.get_absolute_url)

    @property
    def get_next_chapter(self):
        chapterTopics = None
        maxID = Chapter.objects.aggregate(Max('id'))
        if not self.id == maxID['id__max']:
            for i in (self.id + 1,maxID['id__max']):
                try:
                    #chapterTopics = Chapter.objects.get(id = i, link_to=self.link_to)
                    chapterTopics = self.chapter_set.all().get(id = i)

                except Chapter.DoesNotExist:
                    pass
                if chapterTopics:
                    return chapterTopics
            return chapterTopics

    @property
    def get_previous_chapter(self):
        chapterTopics = None
        minID = Chapter.objects.aggregate(Min('id'))
        if not self.id == minID['id__min']:
            for i in (self.id - 1,minID['id__min'],-1):
                try:
                    #chapterTopics = Chapter.objects.get(id = i, link_to=self.link_to)
                    chapterTopics = self.chapter_set.all().get(id = i)
                except Chapter.DoesNotExist:
                    pass
                if chapterTopics:
                    return chapterTopics
            return chapterTopics

    


    @classmethod
    def getChapterSearches(cls, search_input):
        author_searches = cls.objects.filter(
            Q(slug__istartswith = search_input) |
            Q(author__user__username__icontains = search_input) 
        )
        return author_searches




class Like(models.Model):
    link_to = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="likes")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="liked_users")

    # def __str__(self):
    #     return str(self.link_to)

class Comment(models.Model):
    comment_text = models.CharField(max_length=200)
    link_to = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_comments")
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
    def __str__(self):
        return self.user.user.first_name + self.comment_text

    @classmethod
    def createComment(cls, project, profile, comment_text):
        Comment.objects.create(link_to = project, user = profile, timestamp = timezone.now(), comment_text = comment_text)


class Package(models.Model):
    added_on = models.DateTimeField(auto_now_add = True)
    current_chapter = models.ForeignKey(to = Chapter, on_delete = models.CASCADE, null = True)
    profile = models.ForeignKey(to = Profile, on_delete = models.CASCADE, related_name="packages")
    project = models.ForeignKey(to = Project, on_delete = models.CASCADE)
    
    def __str__(self):
        return str(self.profile) + '_' + str(self.project)


class Progress(models.Model):
    chapter = models.ForeignKey(to = Chapter, on_delete = models.CASCADE)
    completed_on = models.DateTimeField(auto_now_add = True)
    package = models.ForeignKey(to = Package, on_delete = models.CASCADE, related_name="progress")
    
    def __str__(self):
        return str(self.package) + '_' + str(self.chapter)

    class Meta:
        verbose_name_plural  = "Progress"

class Suggestion(models.Model):
    content = models.TextField()
    # title = models.CharField(max_length=30,null=True)
    project = models.ForeignKey(to=Project,on_delete=models.CASCADE,null=True)
    chapter = models.ForeignKey(to=Chapter,on_delete=models.CASCADE,null = True,blank=True)
    created_on = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        return self.content

def create_chapter(sender, instance, created,**kwargs):
    # BlogTopics.objects.create(instance)
    if instance.id is not None:
        Project.objects.create(title=str(instance))

def r_pre_save_receiever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        #instance.save()


    
pre_save.connect(r_pre_save_receiever, sender=Project)
pre_save.connect(r_pre_save_receiever, sender=Chapter)
# post_save.connect(create_like_for_blog_topic, sender=BlogTopics)
