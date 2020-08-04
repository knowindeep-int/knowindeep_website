from rest_framework import serializers

from blogs.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['topic','topic_image','topic_content']