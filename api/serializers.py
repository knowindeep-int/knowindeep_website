from rest_framework import serializers

from blogs.models import Project, Comment, Profile, Language, Chapter

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #fields = ['topic','topic_image','topic_content']
        fields = ['image', 'title', 'description']

class CommentSerializer(serializers.ModelSerializer):

    first_name = serializers.SerializerMethodField('first_name_method')
    last_name = serializers.SerializerMethodField('last_name_method')

    def first_name_method(self,comment):
        return comment.user.user.first_name

    def last_name_method(self,comment):
        return comment.user.user.last_name

    class Meta:
        model = Comment
        fields = ['link_to','comment_text','timestamp','user','first_name','last_name']

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ['name']
        

class ProfileSerializer(serializers.ModelSerializer):
    #email_id = serializers.EmailField(required = True)
    # skills = serializers.ListField( 
    # child = serializers.CharField(max_length = 50) 
    # ) 
    #first_name = serializers.CharField(source = 'user.first_name')
    #last_name = serializers.CharField(source = 'user.last_name')
    #email_id = serializers.CharField(source = 'user.email') 
    #profile_id = serializers.PrimaryKeyRelatedField(read_only = True)
    skills_set = LanguageSerializer(many=True, read_only=True)
    #phone_number = serializers.IntegerField()
    
    class Meta:
        model = Profile
        fields = ['user', 'description', 'phone_number','linkedin_id','github_id','twitter_id','isAuthor','account_number','total_earnings','skills_set']
        extra_kwargs = {'skills': {'required': False}, 'user': {'required': False}}
        read_only_fields = ('user',)

    def update(self, instance, validated_data):     
        skills = validated_data.get('skills')
        instance.dp = self.validated_data.get('dp', instance.dp)
        instance.user.email = (validated_data['email_id'], instance.user.email)[validated_data.get('email_id') is None]
        instance.user.last_name = (validated_data['last_name'], instance.user.last_name)[validated_data.get('last_name') is None]
        instance.user.first_name = (validated_data['first_name'],instance.user.first_name)[validated_data.get('first_name') is None]
        instance.description = (self.validated_data['description'], instance.description)[self.validated_data.get('description') is None]
        instance.phone_number = (self.validated_data['phone_number'], instance.phone_number)[self.validated_data.get('phone_number') is None]
        instance.linkedin_id = (self.validated_data['linkedin_id'], instance.linkedin_id)[self.validated_data.get('linkedin_id') is None]
        instance.github_id = (self.validated_data['github_id'], instance.github_id)[self.validated_data.get('github_id') is None]
        instance.twitter_id = (self.validated_data['twitter_id'], instance.twitter_id)[self.validated_data.get('twitter_id') is None]
        instance.isAuthor = self.validated_data.get('isAuthor', instance.isAuthor)
        instance.account_number = (self.validated_data['account_number'], instance.account_number)[self.validated_data.get('account_number') is None]
        instance.total_earnings = (self.validated_data['total_earnings'], instance.total_earnings)[self.validated_data.get('total_earnings') is None]
        
        for skill in skills:
            
            try:
                language = Language.objects.get(name__iexact = skill)
            except Language.DoesNotExist:
                language = Language.objects.create(name = skill.capitalize())

            instance.skills.add(language)

        instance.user.save()
        instance.save()
        return instance

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'