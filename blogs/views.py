from django.shortcuts import render
from .models import Blog, Topic, SubTopic
# Create your views here.
def blogs(request,slug):
    blog= Blog.objects.get(slug=slug)
    context = {'blog':blog}
    return render(request,'new/topics/blog.html',context=context)

def subtopics(request,slug,topic,subtopic):
    blog = Blog.objects.get(slug = slug)
    if blog.canUserView(request.user):
        subtopic_content = SubTopic.objects.get(slug=subtopic)
        subtopics = Topic.getAllSubTopics(slug = topic)
        title = subtopic_content.title
        author = subtopic_content.author

        context = {
            "title":title,
            "chapter_content" : subtopic_content,
            "slug":slug,
            "chapters":subtopics,
            "author": author,
        }
        return render(request,"new/topics/subtopic.html", context)
    return HttpResponse('You are not allowed to access this page', status =500)