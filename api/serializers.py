from rest_framework import serializers

from blogs.models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['topic','topic_image','topic_content']

class CommentSerializer(serializers.ModelSerializer):

    first_name = serializers.SerializerMethodField('first_name_method')
    last_name = serializers.SerializerMethodField('last_name_method')

    def first_name_method(self,comment):
        return comment.user.first_name

    def last_name_method(self,comment):
        return comment.user.last_name

    class Meta:
        model = Comment
        fields = ['link_to','comment_text','timestamp','user','first_name','last_name']