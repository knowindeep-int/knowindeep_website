from django.db import models
from project.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(to =Profile, on_delete = models.CASCADE)
    content = RichTextUploadingField(blank=True,null=True)
    date_approved = models.DateTimeField(default = None, blank =True ,null=True) 
    # description = models.TextField(blank=True,null=True)
    isApproved = models.BooleanField(default=False)
    no_of_views = models.IntegerField(default=0)
    title = models.CharField(max_length = 25, null =False, blank= False)

    def save(self, *args, **kwargs):
        if self.isApproved and self.date_approved is None:
            self.date_approved = timezone.now()
        elif not self.isApprove and self.date_approved is not None:
            self.date_approved = None
        super(Blog,self).save(*args,*kwargs)
    
class Topic(models.Model):
    author = models.ForeignKey(to =Profile, on_delete = models.CASCADE)
    content = RichTextUploadingField(blank=True,null=True)
    title = models.CharField(max_length = 25, null =False, blank= False)
    blog = models.ForeignKey(to = Blog, on_delete = models.CASCADE) 


class SubTopic(models.Model):
    author = models.ForeignKey(to =Profile, on_delete = models.CASCADE)
    content = RichTextUploadingField(blank=True,null=True)
    title = models.CharField(max_length = 25, null =False, blank= False)
    topic = models.ForeignKey(to = Topic, on_delete = models.CASCADE)


