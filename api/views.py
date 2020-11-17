from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


from blogs.models import Project, BlogTopics, Like, Comment, Profile

from .serializers import BlogSerializer, CommentSerializer, ProfileSerializer
from .utils import to_dict

@api_view(['GET',])
def api_detail_blog_view(request,slug):
    
    blog = get_object_or_404(Project,slug=slug)


    if request.method == 'GET':
        if blog is not None:
            serializer = BlogSerializer(blog)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT',])
def api_detail_blog_update_view(request,slug):
    blog = get_object_or_404(Project,slug=slug) 
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

@api_view(['GET',])
def fetchComments(request):
    comments = None
    if request.method == 'GET':
        blog_content_slug = request.GET.get('blog_content_slug')
        blog_content = BlogTopics.objects.get(slug=blog_content_slug)
        comments = Comment.objects.filter(link_to=blog_content).order_by('-timestamp')
        commentSerializer = CommentSerializer(comments, many=True)
        return Response(commentSerializer.data)


@api_view(['POST',])
def api_like_blog_view(request):
    if request.method == 'POST':
        slug = request.POST.get('slug')
        blog = BlogTopics.objects.get(slug=slug)
        data = {}
        try:
            like = Like.objects.get(profile__email_id = request.user.email, link_to=blog)
            like.delete()
            data["success"] = False
            data["likes"] = blog.like_count
            return Response(data=data)  
        except Like.DoesNotExist:
            print(request.user.email)
            profile = Profile.objects.get(email_id = request.user.email)
            like = Like.objects.create(profile=profile, link_to=blog)
            data["success"] = True
            data["likes"] = blog.like_count
            return Response(data=data)
      #  return HttpResponseRedirect(reverse('blogs:blog_post',args=[blog,slug]))

@api_view(['POST',])
def api_comment_blog_view(request):
    data = {}
    data["success"] = False
    if request.method == 'POST':
        slug = request.POST.get('slug')
        blog = BlogTopics.objects.get(slug=slug)
        comment_text = request.POST.get('comment_text')
        comment = Comment.objects.create(link_to=blog,user=request.user,timestamp=timezone.now(),comment_text=comment_text)
        data["success"] = True
        data["user"] = request.user.first_name
        data["comment"] = comment_text
        return Response(data=data)

@api_view(['POST',])
def increase_post_view(request):
    if request.method == "POST":
        slug = request.POST.get('slug')
        blog = None
        try:
            blog = Blog.objects.get(slug=slug)
            blog.increase_view
            return Response({"sucess":"updated","no_of_views":blog.no_of_views})
        except Blog.DoesNotExist:
            return Response({"error":"Some error occured"})

@api_view(['POST',])
def update_profile(request):
    if request.method == "POST":
        print(request.data)
        profile_serializer = ProfileSerializer(data = request.data)
        if not profile_serializer.is_valid():
            print(profile_serializer.errors)
            return Response({'message':profile_serializer.errors}, status = status.HTTP_422_UNPROCESSABLE_ENTITY)
        updated_profile = profile_serializer.update(instance = Profile.objects.get(pk=profile_serializer.data['email_id']), validated_data=request.data)
        #data = {
        #    'profile':model_to_dict(updated_profile)
        #}
        se = ProfileSerializer(updated_profile)
        return Response(se.data, status = status.HTTP_200_OK)


