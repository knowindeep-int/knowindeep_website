from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone

from blogs.models import Blog, BlogTopics, Like, Comment

from .serializers import BlogSerializer

@api_view(['GET',])
def api_detail_blog_view(request,slug):
    
    blog = get_object_or_404(Blog,slug=slug)


    if request.method == 'GET':
        if blog is not None:
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT',])
def api_detail_blog_update_view(request,slug):
    blog = get_object_or_404(Blog,slug=slug) 
    if request.method == "PUT":
        if blog is not None:
            serializer = BlogSerializer(blog,data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "Update successful"
                return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def api_all_detail_view(request):
    blogs = Blog.objects.all()
    if request.method == 'GET':
        if blogs is not None:
            serializer = BlogSerializer(blogs,many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST',])
def api_like_blog_view(request):
    
    # blog = request.get('blog')
    if request.method == 'POST':
        slug = request.POST.get('slug')
        blog = BlogTopics.objects.get(slug=slug)
        data = {}
        try:
            like = Like.objects.get(user = request.user)
            like.delete()
            data["success"] = False
            blog.decreaseLikes()
            data["likes"] = blog.no_of_likes
            return Response(data=data)  
            # return HttpResponseRedirect(reverse('blogs:blog_post',args=[blog,slug]))
        except Like.DoesNotExist:
            like = Like.objects.create(user=request.user, link_to=blog)
            blog.increaseLikes()
            data["success"] = True
            data["likes"] = blog.no_of_likes
            return Response(data=data)
      #  return HttpResponseRedirect(reverse('blogs:blog_post',args=[blog,slug]))

@api_view(['POST',])
def api_comment_blog_view(request):
    data = {}
    data["success"] = False
    print('called comment')
    if request.method == 'POST':
        slug = request.POST.get('slug')
        blog = BlogTopics.objects.get(slug=slug)
        comment_text = request.POST.get('comment_text')
        comment = Comment.objects.create(link_to=blog,user=request.user,timestamp=timezone.now(),comment_text=comment_text)
        data["success"] = True
        data["user"] = request.user.username
        data["comment"] = comment_text
        print("data")
        return Response(data=data)

