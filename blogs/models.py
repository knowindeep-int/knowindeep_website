from django.db import models
from tinymce import HTMLField
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User


class Author(models.Model):
    dp = models.ImageField(null=True,upload_to='profiles/')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=30)
    linkedin_id = models.URLField(max_length=70,null=True,blank=True)
    github_id = models.URLField(max_length=70,null=True,blank=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    topic = models.CharField(max_length=30)
    topic_image = models.ImageField(null=True, upload_to='media/')
    topic_content = models.CharField(max_length=300, blank=True, null=True)
    slug = models.SlugField(null=True,blank=True)
    no_of_views = models.IntegerField(default=0)

    def __str__(self):
        return self.topic

    def increase_view(self):
        self.no_of_views += 1
        self.save()
    


class BlogTopics(models.Model):
    link_to = models.ForeignKey(Blog,on_delete=models.CASCADE, null=True,default=None)
    author_name = models.ForeignKey(Author,on_delete=models.CASCADE, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=40,null=False,blank=False)
   # content = models.CharField(max_length=1000, null=False,blank=False)
    description = models.CharField(max_length=300,blank=True,null=True)
  #  content = HTMLField()
    content = RichTextUploadingField()
    slug = models.SlugField(null=True,blank=True)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    no_of_likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Blog Topics"

    def __str__(self):
        return self.heading

    def get_like_url(self):
        return reverse("api:like-post")
    
    def get_comment_url(self):
        return reverse("api:comment-post")


    @property
    def like_count(self):
        return Like.objects.get(link_to=self).no_of_likes

    def comments(self):
        return Comment.objects.filter(link_to=self)    

    def increaseLikes(self):
        self.no_of_likes += 1
        self.save()

    def decreaseLikes(self):
        self.no_of_likes -= 1
        self.save()
    

class Like(models.Model):
    link_to = models.ForeignKey(BlogTopics, on_delete=models.CASCADE,related_name="likes")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="liked_users")

    def __str__(self):
        return str(self.link_to)

    
class Comment(models.Model):
    link_to = models.ForeignKey(BlogTopics, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    comment_text = models.CharField(max_length=200)
 
    def __str__(self):
        return self.user.username + self.comment_text

    


def create_blog(sender, instance, created,**kwargs):
    # BlogTopics.objects.create(instance)
    if instance.id is not None:
        Blog.objects.create(topic=str(instance))

def save_blog(sender, instance, *args,**kwargs):
    # BlogTopics.objects.create(instance)
    if instance.id is not None:
        print(Blog.objects.create(topic = str(instance)))




# pre_save.connect(save_blog, sender=Blog)
# post_save.connect(save_blog, sender=Blog)



def r_pre_save_receiever(sender,instance,*args,**kwargs):
    print('saving')
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

  

pre_save.connect(r_pre_save_receiever, sender=Blog)
pre_save.connect(r_pre_save_receiever, sender=BlogTopics)
# post_save.connect(create_like_for_blog_topic, sender=BlogTopics)
