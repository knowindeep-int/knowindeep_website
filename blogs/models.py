from django.db import models
from tinymce import HTMLField
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, int_list_validator, MaxValueValidator
from django.db.models import Max, Min

from django.contrib.auth.models import User


class Profile(models.Model):
    dp = models.ImageField(null=True,upload_to='profiles/')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=30)
    phone_number = models.IntegerField(unique=True, validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    linkedin_id = models.URLField(max_length=70,null=True,blank=True)
    github_id = models.URLField(max_length=70,null=True,blank=True)
    twitter_id = models.URLField(max_length=70, null=True, blank=True)
    isAuthor = models.BooleanField(default=False)
    account_number = models.CharField(max_length=30, null=True, blank=True)
    total_earnings = models.IntegerField()

    def __str__(self):
        return self.name


class Project(models.Model):
    # topic = models.CharField(max_length=30)
    # topic_image = models.ImageField(null=True, upload_to='media/')
    # topic_content = models.CharField(max_length=300, blank=True, null=True)
    slug = models.SlugField(null=True,blank=True)
    no_of_views = models.IntegerField(default=0)


    # update
    image = models.ImageField(null=True,upload_to='project/')
    title = models.CharField(max_length=25)
    overview = models.CharField(max_length=300)
    pre_req = models.CharField(max_length=300)


    def __str__(self):
        return self.title

    @property
    def increase_view(self):
        self.no_of_views += 1
        self.save()



class BlogTopics(models.Model):
    link_to = models.ForeignKey(Project,on_delete=models.CASCADE, null=True,default=None)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=40,null=False,blank=False)
   # content = models.CharField(max_length=1000, null=False,blank=False)
    description = models.CharField(max_length=300,blank=True,null=True)
  #  content = HTMLField()
  # new comment
    content = RichTextUploadingField(blank=True,null=True)
    slug = models.SlugField(null=True,blank=True)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    # no_of_likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Blog Topics"

    def __str__(self):
        return self.heading

    def get_like_url(self):
        return reverse("api:like-post")

    def get_comment_url(self):
        return reverse("api:comment-post")

    @property
    def get_next_blog(self):
        blogTopics = None
        maxID = BlogTopics.objects.aggregate(Max('id'))
        if not self.id == maxID['id__max']:
            for i in (self.id + 1,maxID['id__max']):
                try:
                    blogTopics = BlogTopics.objects.get(id = i, link_to=self.link_to)
                except BlogTopics.DoesNotExist:
                    pass
                if blogTopics:
                    return blogTopics
            return blogTopics

    @property
    def get_previous_blog(self):
        blogTopics = None
        minID = BlogTopics.objects.aggregate(Min('id'))
        if not self.id == minID['id__min']:
            for i in (self.id - 1,minID['id__min'],-1):
                try:
                    blogTopics = BlogTopics.objects.get(id = i, link_to=self.link_to)
                except BlogTopics.DoesNotExist:
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
                self.likes.get(user=user)
                return True
            except Like.DoesNotExist:
                has_liked = False
                return False


class Like(models.Model):
    link_to = models.ForeignKey(BlogTopics, on_delete=models.CASCADE,related_name="likes")
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="liked_users")

    def __str__(self):
        return str(self.link_to)


class Comment(models.Model):
    link_to = models.ForeignKey(BlogTopics, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username + self.comment_text




def create_blog(sender, instance, created,**kwargs):
    # BlogTopics.objects.create(instance)
    if instance.id is not None:
        Project.objects.create(title=str(instance))


def r_pre_save_receiever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()



pre_save.connect(r_pre_save_receiever, sender=Project)
pre_save.connect(r_pre_save_receiever, sender=BlogTopics)
# post_save.connect(create_like_for_blog_topic, sender=BlogTopics)
