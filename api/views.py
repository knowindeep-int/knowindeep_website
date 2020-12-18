from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blogs.models import Project, Chapter, Like, Comment, Profile

from knowindeep import Constants

from .serializers import ProjectSerializer, CommentSerializer, ProfileSerializer, ChapterSerializer

@api_view(['GET',])
def api_detail_chapter_view(request,slug):
    
    project = get_object_or_404(Project,slug=slug)


    if request.method == 'GET':
        if project is not None:
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT',])
def api_detail_chapter_update_view(request,slug):
    project = get_object_or_404(Project,slug=slug) 
    if request.method == "PUT":
        if project is not None:
            serializer = ProjectSerializer(project,data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "Update successful"
                return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET',])
def api_all_detail_view(request):
    projects = Project.objects.all()
    if request.method == 'GET':
        if projects is not None:
            serializer = ProjectSerializer(projects,many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET',])
def fetchComments(request):
    comments = None
    if request.method == 'GET':
        chapter_content_slug = request.GET.get('chapter_content_slug')
        #blog_content = Chapter.objects.get(slug=blog_content_slug)
        #comments = Comment.objects.filter(link_to=blog_content).order_by('-timestamp')
        comments = Chapter.getAllComments(chapter_content_slug)
        commentSerializer = CommentSerializer(comments, many=True)
        return Response(commentSerializer.data)


@api_view(['POST',])
def api_like_chapter_view(request):
    if request.method == 'POST':
        slug = request.POST.get('slug')
        chapter = Chapter.objects.get(slug=slug)
        data = {}
        try:
            like = Like.objects.get(profile__user__email = request.user.email, link_to=chapter)
            #like = Like.objects.get(link_to = chapter, profile__user__email = 'dev.krishang.09@gmail.comewfewfvrfewefefe4feferfrr')
            #like = Like.objects.getlink_to = chapter)
            like.delete()
            data["success"] = False
            data["likes"] = chapter.like_count
            return Response(data=data)  
        except Like.DoesNotExist:
            profile = Profile.objects.get(user__email = request.user.email)
            like = Like.objects.create(profile=profile, link_to=chapter)
            data["success"] = True
            data["likes"] = chapter.like_count
            return Response(data=data)
      #  return HttpResponseRedirect(reverse('blogs:blog_post',args=[ ,slug]))

@api_view(['POST',])
def api_comment_chapter_view(request):
    data = {}
    data["success"] = False
    if request.method == 'POST':
        slug = request.POST.get('slug')
        chapter = Chapter.getChapter(slug = slug)
        comment_text = request.POST.get('comment_text')
        profile = Profile.getProfile(user = request.user)
        comment = Comment.createComment(chapter = chapter, profile = profile, comment_text = comment_text)
        data["success"] = True
        data["user"] = request.user.first_name + request.user.last_name
        data["comment"] = comment_text
        return Response(data=data)

@api_view(['POST',])
def increase_post_view(request):
    if request.method == "POST":
        slug = request.POST.get('slug')
        project = None
        try:
            project = Project.objects.get(slug=slug)
            project.increase_view
            return Response({Constants.SUCCESS:"updated","no_of_views":project.no_of_views})
        except Project.DoesNotExist:
            return Response({Constants.ERROR:"Some error occured"})


@api_view(['POST',])
def update_profile(request):
    if request.method == "POST":
        profile_serializer = ProfileSerializer(data = request.data)
        if not profile_serializer.is_valid():
            return Response({'message':profile_serializer.errors}, status = status.HTTP_422_UNPROCESSABLE_ENTITY)
        updated_profile = profile_serializer.update(instance = Profile.objects.get(pk=request.data['profile_id']), validated_data=request.data)
        se = ProfileSerializer(updated_profile)
        return Response(se.data, status = status.HTTP_200_OK)

@api_view(['GET',])
def search_project(request):
    if request.method == "GET":
        search_input = request.GET['search_input']
        project_searches = Project.getProjectSearches(search_input = search_input)
        author_searches = Profile.getAuthorSearches(search_input = search_input)
        chapter_searches = Chapter.getChapterSearches(search_input = search_input)

        project_searches_serializer = ProjectSerializer(project_searches[:3], many = True)
        author_searches_serializer = ProfileSerializer(author_searches[:3], many = True)
        chapter_searches_serializer = ChapterSerializer(chapter_searches[:3], many = True)
    
        data = {
            "projects": project_searches_serializer.data, 
            "authors": author_searches_serializer.data, 
            "chapters": chapter_searches_serializer.data
        }

        return Response(data, status = status.HTTP_200_OK)

@api_view(['POST',])
def api_save_draft(request):
    if request.method == "POST":
        pk = request.POST.get('pk', None)
        if pk == "":
            pk = None
        
        user = Profile.objects.get(user = request.user)
    
        if pk is None:
            project = Project(author = user, title = "random")  #why error in case of using create ?Max recursion depth??
            project.save()
        else:
            project = Project.objects.get(pk = pk)
        
        project_serializer = ProjectSerializer(data = request.data)
        
        if not project_serializer.is_valid():
            return Response(project_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        updated_project = project_serializer.update(instance = project)

        pk = project.pk
        data = {
            'success': "Project updated successfully!", 
            'pk': pk
        }
        return Response(data, status = status.HTTP_200_OK)

import json
@api_view(['POST',])
def api_save_chapter_draft(request):
    if request.method == "POST":
        pk = request.data['pk']
        project = Project.objects.get(pk = pk)
            
        chapter_serializer = ChapterSerializer(data = json.loads(request.data['chapters']), many = True, partial=True)
        if not chapter_serializer.is_valid():
            return Response(chapter_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        chapter_serializer.save()
        return Response(chapter_serializer.data, status = status.HTTP_200_OK)