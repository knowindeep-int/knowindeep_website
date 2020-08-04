from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from blogs.models import Blog

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
    print(request.data)
    if request.method == "PUT":
        if blog is not None:
            serializer = BlogSerializer(blog,data=request.data)
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["success"] = "Update successful"
                return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
