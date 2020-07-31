from django.db import models
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.utils import timezone

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=30)

class BlogTopics(models.Model):
    id = models.AutoField(primary_key=True)
    link_to = models.ForeignKey(Blog,on_delete=models.CASCADE)
    author_name = models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=40)
    content = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Blog Topics"

class Like(models.Model):
    link_to = models.ForeignKey(BlogTopics, on_delete=models.CASCADE)
    no_of_likes = models.IntegerField(default=0)

class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=30)
    comment_text = models.CharField(max_length=200)






# def r_pre_save_receiever(sender,instance,*args,**kwargs):
#     print('saving')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()

  

# pre_save.connect(r_pre_save_receiever, sender=Restaurant)