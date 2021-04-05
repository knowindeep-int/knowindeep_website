from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.core.mail import send_mail
from project.models import Project, Chapter, Like, Comment, Profile, Language, Suggestion
from django.contrib.auth.models import User
from knowindeep import Constants
import os
from blogs.models import Blog,SubTopic
from .serializers import ProjectSerializer, CommentSerializer, ProfileSerializer, ChapterSerializer, LanguageSerializer, SuggestionSerializer, BlogSerializer
from dotenv import load_dotenv
load_dotenv()


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
        project_slug = request.GET.get('project_slug')
        #blog_content = Chapter.objects.get(slug=blog_content_slug)
        #comments = Comment.objects.filter(link_to=blog_content).order_by('-timestamp')
        comments = Project.getAllComments(project_slug)
        commentSerializer = CommentSerializer(comments, many=True)
        return Response(commentSerializer.data)


@api_view(['POST',])
def api_like_chapter_view(request):
    if request.method == 'POST':
        slug = request.POST.get('slug')
        project = Project.objects.get(slug=slug)
        data = {}
        try:
            like = Like.objects.get(profile__user__email = request.user.email, link_to=project)
            #like = Like.objects.get(link_to = chapter, profile__user__email = 'dev.krishang.09@gmail.comewfewfvrfewefefe4feferfrr')
            #like = Like.objects.getlink_to = chapter)
            like.delete()
            data["success"] = False
            data["likes"] = project.like_count
            return Response(data=data)  
        except Like.DoesNotExist:
            profile = Profile.objects.get(user__email = request.user.email)
            like = Like.objects.create(profile=profile, link_to=project)
            data["success"] = True
            data["likes"] = project.like_count
            return Response(data=data)
      #  return HttpResponseRedirect(reverse('blogs:blog_post',args=[ ,slug]))

@api_view(['POST',])
def api_comment_project_view(request):
    data = {}
    data["success"] = False
    if request.method == 'POST':
        slug = request.POST.get('slug')
        project = Project.getProject(slug = slug)
        comment_text = request.POST.get('comment_text')
        profile = Profile.getProfile(user = request.user)
        comment = Comment.createComment(project = project, profile = profile, comment_text = comment_text)
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
        profile = Profile.objects.get(pk=request.POST.get('profile_id'))
        if request.POST.get('field') == "username":
            profile.user.username =  request.POST.get('value')
            profile.user.save()
        # value = getattr(profile, request.POST.get('value'))
        else:
            setattr(profile, request.POST.get('field'), request.POST.get('value'))
        profile.save()
        # print(Profile.objects.get(pk=request.POST.get('profile_id')))
        # print(getattr(Profile.objects.get(pk=request.POST.get('profile_id')),'description'))
        # profile_serializer = ProfileSerializer(data = request.data)
        # if not profile_serializer.is_valid():
            # print(profile_serializer.errors)
            # return Response({'message':profile_serializer.errors}, status = status.HTTP_422_UNPROCESSABLE_ENTITY)
        # updated_profile = profile_serializer.update(instance = Profile.objects.get(pk=request.POST.get('profile_id')), validated_data=request.data)
        se = ProfileSerializer(profile)
        print(se.data)
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

@api_view(['GET',])
def api_search_languages(request):
    if request.method == "GET":
        search_input = request.GET['search_input']
        language_searches = Language.getLanguageSearches(search_input = search_input)
        language_serializer = LanguageSerializer(language_searches, many = True)

        data = {
            'languages':language_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

@api_view(['POST', 'GET',])
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
        print(request.data)
        if not project_serializer.is_valid():
            return Response(project_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        updated_project = project_serializer.update(instance = project, data = request.data)
        pk = project.pk
        data = {
            'success': "Project updated successfully!", 
            'pk': pk
        }
        return Response(data, status = status.HTTP_200_OK)
    
    if request.method == 'GET':
        pk = request.GET['pk']
        if pk is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            project = Project.objects.get(pk = pk)
        
        project_draft = ProjectSerializer(project)
        data = {
            'project_draft': project_draft.data,
        }
        return Response(data, status = status.HTTP_200_OK)

import json
@api_view(['POST',])
def api_save_chapter_draft(request):
    if request.method == "POST":
        pk = request.data['pk']
        project = Project.objects.get(pk = pk)
        project.chapters.all().delete()
        print(request.data)
        chapter_serializer = ChapterSerializer(data = json.loads(request.data['chapters']), many = True, partial=True)
        #chapter_serializer = ChapterSerializer(data = request.data['chapters'], many = True, partial=True)
        
        if not chapter_serializer.is_valid():
            return Response(chapter_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        chapter_serializer.save()
        return Response(chapter_serializer.data, status = status.HTTP_200_OK)

@api_view(['POST',])
def api_delete_lang(request):
    if request.method == 'POST':
        print(request.data)
        project = Project.objects.get(pk = request.POST['pk'])
        language = Language.objects.get(name = request.POST['name'])
        project.languages.remove(language)
        data = {
            'message':'deleted successfully',
            'pk': request.POST['pk'] 
        }
        return Response(data,status=status.HTTP_200_OK)


@api_view(['GET',])
def api_get_languages_prereqs(request):
    if request.method == "GET":
        lang =  Project.objects.get(pk = request.GET['pk']).languages
        pre = Project.objects.get(pk = request.GET['pk']).pre_req
        print(lang)
        lang_serializer = LanguageSerializer(lang, many=True)
        # pre_serializer = PreRequisiteSerializer(pre, many=True)
    
        data = {
                'languages': lang_serializer.data, 
                'prerequisites': pre
            }

        return Response(data, status = status.HTTP_200_OK)

@api_view(['POST',])
def api_create_project(request):
    if request.method == 'POST':
        pk = request.POST.get("pk")
        if pk is None:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            project = Project.get_project(pk)
        
        project.complete_project
        updated_project = ProjectSerializer(project)
        return Response(updated_project.data, status = status.HTTP_200_OK)

@api_view(['GET',])
def api_get_project_absolute_url(request):
    if request.method == "GET":
        slug = request.GET.get('slug')

        project = Project.objects.get(slug = slug)
        url = project.get_absolute_url()
        
        data = {
            'url': url  
        }

        return Response(data, status = status.HTTP_200_OK)

@api_view(['GET',])
def api_get_chapter_absolute_url(request):
    if request.method == "GET":
        project_slug = request.GET.get('project_slug')
        chapter_slug = request.GET.get('chapter_slug')

        url = Chapter.get_chapter_absolute_url(chapter_slug = chapter_slug, project_slug = project_slug, request = request)
        
        data = {
            'url': url  
        }

        return Response(data, status = status.HTTP_200_OK)

@api_view(['POST',])
def api_create_chapter(request):
    if request.method == "POST":

        print(request.data)

        chapter_pk = request.POST.get('chapter_pk', None)

        if chapter_pk == "":
            chapter_pk = None

        pk = request.POST.get('link_to', None)
        chapter_serializer = ChapterSerializer(data = request.data)

        if not chapter_serializer.is_valid():
            print(chapter_serializer.data)
            print(chapter_serializer.errors)
            return Response(chapter_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        if chapter_pk is None:
            chapter_serializer.save()
            chapter_pk = chapter_serializer.data['id']

        else:
            chapter_serializer.update(chapter_instance= Chapter.objects.get(pk = chapter_pk))
            # print(chapter_serializer.data['id'])
        data = {
            'success': 'Chapter saved successfully!',
            'pk': pk,
            'chapter_pk': chapter_pk
        }

        return Response(data, status = status.HTTP_200_OK)

@api_view(['POST',])
def api_update_status(request):
    if request.method == "POST":
        pk = request.POST.get('link_to')
        print(pk)
        project = Project.objects.get(pk= pk)
        project.status = 'teach'
        project.save()
        print(project.status)
        return Response(pk,status=status.HTTP_200_OK)

@api_view(['POST',])
def api_create_suggestion(request):
    if request.method == "POST":

        pk = request.POST['project']
        project = Project.objects.get(pk = pk)
        email_id = project.author.user.email
        suggestion = SuggestionSerializer(data = request.data)
        
        if not suggestion.is_valid():
            print(suggestion.errors)
            return Response(suggestion.errors,status=status.HTTP_400_BAD_REQUEST)
        
        suggestion.save()
        
        send_mail('Suggestions - Suggested from KnowInDeep',
        suggestion.data['content'],
        os.getenv('EMAIL_HOST_USER'),
        [email_id],
        fail_silently=False,    
        )
        data = {'success':'suggestion made successfully','pk':request.POST['project']}
        return Response(data,status=status.HTTP_200_OK)

@api_view(['POST',])
def api_resolve_suggestion(request):
    if request.method == "POST":
        pk = request.POST['pk']
        # project = Project.objects.get(pk = pk)
        suggestions = Suggestion.objects.get(pk = pk)
        suggestions.delete()
        data = {'success':'suggestion resolved successfully','pk':request.POST['pk']}
        return Response(data,status=status.HTTP_200_OK)

@api_view(['GET',])
def api_get_suggestion(request):
    if request.method == "GET":
        pk = request.GET.get('project', None)
        chapter_pk = request.GET.get('chapter', None)

        if pk is not None :
            suggestions = Suggestion.objects.filter(project = pk)
        else:
            suggestions = Suggestion.objects.filter(chapter = chapter_pk)
        
        sug = SuggestionSerializer(suggestions,many = True)
        data = {'suggestions':sug.data,'pk':pk}
        return Response(data,status= status.HTTP_200_OK)

@api_view(['POST',])
def api_create_bookmark(request):
    if request.method == 'POST' and request.POST['method']=='project':
        pk= request.POST['pk']
        project = Project.objects.get(pk = pk)
        profile = Profile.objects.get(user = request.user)
        project.bookmark.add(profile)
        
        data = {
            'message':'created successfully',
            'pk': pk,
            'count': project.bookmark.all().count()
        }
        return Response(data,status=status.HTTP_200_OK)
    if request.method == 'POST' and request.POST['method']=='blog':
        pk= request.POST['pk']
        project = Blog.objects.get(pk = pk)
        profile = Profile.objects.get(user = request.user)
        project.bookmark.add(profile)
        
        data = {
            'message':'created successfully',
            'pk': pk,
            'count': project.bookmark.all().count()
        }
        return Response(data,status=status.HTTP_200_OK)


@api_view(['POST',])
def api_delete_bookmark(request):
    if request.method == 'POST' and request.POST['method']=='project':
        pk= request.POST['pk']
        project = Project.objects.get(pk = pk)
        profile = Profile.objects.get(user = request.user)
        project.bookmark.remove(profile)
        data = {
            'message':'deleted successfully',
            'pk': pk,
            'count': project.bookmark.all().count(),
        }
        return Response(data,status=status.HTTP_200_OK)
    if request.method == 'POST' and request.POST['method']=='blog':
        pk= request.POST['pk']
        project = Blog.objects.get(pk = pk)
        profile = Profile.objects.get(user = request.user)
        project.bookmark.remove(profile)
        data = {
            'message':'deleted successfully',
            'pk': pk,
            'count': project.bookmark.all().count(),
        }
        return Response(data,status=status.HTTP_200_OK)

@api_view(['POST',])
def api_create_chapter_bookmark(request):
    if request.method == 'POST' and request.POST['method']=='blog':
        pk= request.POST['pk']
        chapter = Chapter.objects.get(pk = pk)
        profile = Profile.objects.get(user = request.user)
        chapter.bookmark.add(profile)
        
        data = {
            'message':'created successfully',
            'pk': pk,
            'count': chapter.bookmark.all().count()
        }
        return Response(data,status=status.HTTP_200_OK)
    if request.method == 'POST' and request.POST['method']=='subtopic':
        pk= request.POST['pk']
        chapter = SubTopic.objects.get(pk = pk)
        profile = Profile.objects.get(user = request.user)
        chapter.bookmark.add(profile)
        
        data = {
            'message':'created successfully',
            'pk': pk,
            'count': chapter.bookmark.all().count()
        }
        return Response(data,status=status.HTTP_200_OK)


@api_view(['POST',])
def api_delete_chapter_bookmark(request):
    if request.method == 'POST' and request.POST['method']=='chapter':
        pk= request.POST['pk']
        chapter = Chapter.objects.get(pk = pk)
        profile = Profile.objects.get(user = request.user)
        chapter.bookmark.remove(profile)
        data = {
            'message':'deleted successfully',
            'pk': pk,
            'count': chapter.bookmark.all().count(),
        }
        return Response(data,status=status.HTTP_200_OK)
    if request.method == 'POST' and request.POST['method']=='subtopic':
        pk= request.POST['pk']
        chapter = SubTopic.objects.get(pk = pk)
        profile = Profile.objects.get(user = request.user)
        chapter.bookmark.remove(profile)
        data = {
            'message':'deleted successfully',
            'pk': pk,
            'count': chapter.bookmark.all().count(),
        }
        return Response(data,status=status.HTTP_200_OK)

@api_view(['GET',])
def api_get_ch_pr_au(request):
    if request.method == 'GET':
        chapter = Chapter.objects.all()
        project = Project.objects.all()
        author = Profile.objects.all()
        chapters = ChapterSerializer(chapter,many = True)
        projects = ProjectSerializer(project,many = True)
        authors = ProfileSerializer(author,many = True) 
        data={
            'chapter':chapters.data,
            'author':authors.data,
            'project':projects.data,
        }
        return Response(data,status=status.HTTP_200_OK)


@api_view(['GET',])
def api_get_blogs(request):
    if request.method == 'GET':
        print('rerg')
        pk = request.GET['pk']
        blog = Blog.objects.get(pk=pk)
        blog_serializer = BlogSerializer(blog)  
        data = {'blog':blog_serializer.data}      
        return Response(data, status=status.HTTP_200_OK)