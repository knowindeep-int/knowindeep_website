from django.db import models
from tinymce import HTMLField
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.db.models.signals import post_save, pre_save
from django.utils import timezone

class Blog(models.Model):
   # id = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length=30)
    slug = models.SlugField(null=True,blank=True)
    # con = HTMLField(default = '')

    def __str__(self):
        return self.topic


class BlogTopics(models.Model):
   # id = models.IntegerField(primary_key=True,auto_created=True)
    link_to = models.ForeignKey(Blog,on_delete=models.CASCADE, null=True,default=None)
    author_name = models.CharField(max_length=30, null=False,blank=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=40,null=False,blank=False)
    content = models.CharField(max_length=1000, null=False,blank=False)
    slug = models.SlugField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Blog Topics"

    def __str__(self):
        return self.heading

    @property
    def like_count(self):
        return Like.objects.get(link_to=self).no_of_likes

    def comments(self):
        return Comment.objects.filter(link_to=self)    
    

class Like(models.Model):
    link_to = models.ForeignKey(BlogTopics, on_delete=models.CASCADE,related_name="likes")
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.link_to)

    
class Comment(models.Model):
    link_to = models.ForeignKey(BlogTopics, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=30)
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name + self.comment_text

    


def create_blog(sender, instance, created,**kwargs):
    # BlogTopics.objects.create(instance)
    if instance.id is not None:
        Blog.objects.create(topic=str(instance))

def save_blog(sender, instance, *args,**kwargs):
    # BlogTopics.objects.create(instance)
    if instance.id is not None:
        print(Blog.objects.create(topic = str(instance)))

def create_like_for_blog_topic(sender,instance,*args,**kwargs):
    if instance.likes.all().count() == 0:
        instance.likes.create()

# pre_save.connect(save_blog, sender=Blog)
# post_save.connect(save_blog, sender=Blog)



def r_pre_save_receiever(sender,instance,*args,**kwargs):
    print('saving')
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        instance.save()

  

pre_save.connect(r_pre_save_receiever, sender=Blog)
pre_save.connect(r_pre_save_receiever, sender=BlogTopics)
post_save.connect(create_like_for_blog_topic, sender=BlogTopics)