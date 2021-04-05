from django.db import models
from project.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.db.models.signals import post_save, pre_save
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(to =Profile, on_delete = models.CASCADE)
    content = RichTextUploadingField(blank=True,null=True)
    date_approved = models.DateTimeField(default = None, blank =True ,null=True) 
    image = models.URLField(max_length=200,blank=True,null=True)
    # description = models.TextField(blank=True,null=True)
    bookmark = models.ManyToManyField(to=Profile,blank=True,related_name='bookmarks_blog')
    isCompleted = models.BooleanField(default = False) 
    isApproved = models.BooleanField(default=False)
    slug = models.SlugField(null=True,blank=True)
    no_of_views = models.IntegerField(default=0)
    title = models.CharField(max_length = 25, null =False, blank= False)

    def save(self, *args, **kwargs):
        if self.isApproved and self.date_approved is None:
            self.date_approved = timezone.now()
        elif not self.isApproved and self.date_approved is not None:
            self.date_approved = None
        super(Blog,self).save(*args,*kwargs)
        
    @property
    def get_absolute_url(self): 
        return reverse('project:sub_topic', kwargs={'slug': self.slug})
    @property
    def getCompleteUrl(self):
        if settings.DEBUG:
            return "http://%s/blogs%s" % ('127.0.0.1:8000' ,self.get_absolute_url)
        else:
            return "https://%s/blogs%s" % ('127.0.0.1:8000' ,self.get_absolute_url)


    def canUserView(self, user):
        return self.isApproved or user.is_superuser    
class Topic(models.Model):
    author = models.ForeignKey(to =Profile, on_delete = models.CASCADE)
    content = RichTextUploadingField(blank=True,null=True)
    title = models.CharField(max_length = 25, null =False, blank= False)
    blog = models.ForeignKey(to = Blog, on_delete = models.CASCADE,related_name='topics')
    slug = models.SlugField(null=True,blank=True)
 

    @classmethod
    def getAllSubTopics(cls, slug):
        topic = cls.objects.get(slug = slug)
        return topic.subtopics.all()


class SubTopic(models.Model):
    author = models.ForeignKey(to =Profile, on_delete = models.CASCADE)
    bookmark = models.ManyToManyField(to=Profile,blank=True,related_name='bookmarks_sub')
    content = RichTextUploadingField(blank=True,null=True)
    title = models.CharField(max_length = 25, null =False, blank= False)
    topic = models.ForeignKey(to = Topic, on_delete = models.CASCADE,related_name='subtopics')
    slug = models.SlugField(null=True,blank=True)


def r_pre_save_receiever(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        print(instance.slug)
        #instance.save()

pre_save.connect(r_pre_save_receiever, sender=Blog)
pre_save.connect(r_pre_save_receiever, sender=Topic)
pre_save.connect(r_pre_save_receiever, sender=SubTopic)

