from django.db import models
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

from knowindeep import Constants

class Language(models.Model):
    name = models.CharField(max_length = 100,unique = True, primary_key = True)
    is_available = models.BooleanField(null = True, blank = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural  = "Language"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dp = models.ImageField(null=True,upload_to='profiles/')
    name = models.CharField(max_length=30, null = True, unique=True)
    description = models.CharField(max_length=200, null = True)
    email_id = models.EmailField(max_length=30, unique=True, primary_key=True)
    phone_number = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    linkedin_id = models.URLField(max_length=70,null=True,blank=True)
    github_id = models.URLField(max_length=70,null=True,blank=True)
    twitter_id = models.URLField(max_length=70, null=True, blank=True)
    isAuthor = models.BooleanField(default=False)
    account_number = models.CharField(max_length=30, null=True, blank=True)
    total_earnings = models.IntegerField(null=True, blank=True)
    skills = models.ManyToManyField(to = Language, related_name="skills")

    def __str__(self):
        return self.name

    @classmethod
    def getUser(cls, name):
        profile = cls(name = name)
        return profile.user
        

    @property
    def skills_set(self):
        return self.skills.all()

class PreRequisite(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Pre-Requisites"


class Project(models.Model):
     # topic = models.CharField(max_length=30)
    # topic_image = models.ImageField(null=True, upload_to='media/')
    # topic_content = models.CharField(max_length=300, blank=True, null=True)
    slug = models.SlugField(null=True,blank=True)
    no_of_views = models.IntegerField(default=0)
    description = models.TextField(null = True, blank = True)
    author = models.ForeignKey(to = Profile, on_delete = models.CASCADE)
    no_of_hours = models.DecimalField(null = True, blank = True, decimal_places = 1, max_digits = 4)
    difficulty_level = models.CharField(max_length = 100,null = True, blank = True, choices = ((Constants.EASY, Constants.EASY),(Constants.MEDIUM, Constants.MEDIUM), (Constants.HARD, Constants.HARD)))
    isApproved = models.BooleanField(default=False)
    languages = models.ManyToManyField(to = Language)
    # update
    image = models.ImageField(null=True,upload_to='project/')
    title = models.CharField(max_length=25)
    overview = models.CharField(max_length=300)
    pre_req = models.ManyToManyField(to = PreRequisite)

    def __str__(self):
        return self.title

    @classmethod
    def getTitle(cls, slug):
        project = cls.objects.get(slug = slug)
        return project.title

    @classmethod
    def getAllChapters(cls, slug):
        project = cls.objects.get(slug = slug)
        return project.chapter_set.all()

    @property
    def increase_view(self):
        self.no_of_views += 1
        self.save()

    @classmethod
    def get_popular_projects(KClass):
        return KClass.objects.all().order_by('-no_of_views')[:5]

    @classmethod
    def get_popular_approved_projects(KClass):
        return KClass.objects.filter(isApproved = True).order_by('-no_of_views')[:5]



class Chapter(models.Model):
    link_to = models.ForeignKey(Project,on_delete=models.CASCADE, null=True,default=None)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=40,null=False,blank=False)
   # content = models.CharField(max_length=1000, null=False,blank=False)
    description = models.CharField(max_length=300,blank=True,null=True)
  #  content = HTMLField()  .
    content = RichTextUploadingField(blank=True,null=True)
    slug = models.SlugField(null=True,blank=True)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    # no_of_likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Chapters"

    def __str__(self):
        return self.heading

    def get_like_url(self):
        return reverse("api:like-post")

    def get_comment_url(self):
        return reverse("api:comment-post")

    @property
    def get_next_blog(self):
        blogTopics = None
        maxID = Chapter.objects.aggregate(Max('id'))
        if not self.id == maxID['id__max']:
            for i in (self.id + 1,maxID['id__max']):
                try:
                    blogTopics = Chapter.objects.get(id = i, link_to=self.link_to)
                except Chapter.DoesNotExist:
                    pass
                if blogTopics:
                    return blogTopics
            return blogTopics

    @property
    def get_previous_blog(self):
        blogTopics = None
        minID = Chapter.objects.aggregate(Min('id'))
        if not self.id == minID['id__min']:
            for i in (self.id - 1,minID['id__min'],-1):
                try:
                    blogTopics = Chapter.objects.get(id = i, link_to=self.link_to)
                except Chapter.DoesNotExist:
                    pass
                if blogTopics:
                    return blogTopics
            return blogTopics

    @property
    def like_count(self):
        return Like.objects.filter(link_to=self).count()

    def comments(self):
        return Comment.objects.filter(link_to=self)

    def increaseLikes(self):
        self.no_of_likes += 1
        self.save()

    def decreaseLikes(self):
        self.no_of_likes -= 1
        self.save()

    def has_user_liked(self,user):
        if not user.is_anonymous:
            try:
                isLiked = Like.objects.get(profile__email_id=user.email,link_to=self)
                # self.likes.get(profile.email_id == user.email)
                return True
            except Like.DoesNotExist:
                has_liked = False
                return False

    @classmethod
    def getAllComments(cls, blog_content_slug):
        blog = cls.objects.get(slug = blog_content_slug)
        return blog.comment_set.all().order_by('-timestamp')

class Like(models.Model):
    link_to = models.ForeignKey(Chapter, on_delete=models.CASCADE,related_name="likes")
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="liked_users")

    # def __str__(self):
    #     return str(self.link_to)



class Comment(models.Model):
    link_to = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.user.name + self.comment_text


def create_blog(sender, instance, created,**kwargs):
    # BlogTopics.objects.create(instance)
    if instance.id is not None:
        Project.objects.create(title=str(instance))


def r_pre_save_receiever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()



pre_save.connect(r_pre_save_receiever, sender=Project)
pre_save.connect(r_pre_save_receiever, sender=Chapter)
# post_save.connect(create_like_for_blog_topic, sender=BlogTopics)
