from rest_framework import serializers

from blogs.models import Project, Comment, Profile, Language

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
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

class ProfileSerializer(serializers.ModelSerializer):
    email_id = serializers.EmailField(required = True)
    skills = serializers.ListField( 
    child = serializers.CharField(max_length = 50) 
    ) 
    #phone_number = serializers.IntegerField()
    
    class Meta:
        model = Profile
        fields = '__all__'
        
    def update(self, instance):       
        instance.dp = self.validated_data.get('dp', instance.dp)        
        instance.name = (self.validated_data['name'],instance.name)[self.validated_data.get('name') is None]
        instance.description = (self.validated_data['description'], instance.description)[self.validated_data.get('description') is None]
        instance.phone_number = (self.validated_data['phone_number'], instance.phone_number)[self.validated_data.get('phone_number') is None]
        instance.linkedin_id = (self.validated_data['linkedin_id'], instance.linkedin_id)[self.validated_data.get('linkedin_id') is None]
        instance.github_id = (self.validated_data['github_id'], instance.github_id)[self.validated_data.get('github_id') is None]
        instance.twitter_id = (self.validated_data['twitter_id'], instance.twitter_id)[self.validated_data.get('twitter_id') is None]
        instance.isAuthor = self.validated_data.get('isAuthor', instance.isAuthor)
        instance.account_number = (self.validated_data['account_number'], instance.account_number)[self.validated_data.get('account_number') is None]
        instance.total_earnings = (self.validated_data['total_earnings'], instance.total_earnings)[self.validated_data.get('total_earnings') is None]
        
        for skill in self.validated_data['skills']:
            
            try:
                language = Language.objects.get(name__iexact = skill)
            except Language.DoesNotExist:
                language = Language.objects.create(name = skill.capitalize())

            instance.skills.add(language)

        
        instance.save()
        return instance