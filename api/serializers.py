from rest_framework import serializers

from blogs.models import Project, Comment, Profile, Language, Chapter

class ProjectSerializer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=True, allow_null=True, required = False, max_length = 25)
    class Meta:
        model = Project
        #fields = ['topic','topic_image','topic_content']
        fields = ['image', 'title', 'description', 'slug']
        extra_kwargs = {'slug': {'required': False}, 'title': {'required': False}}

    def update(self, instance):
        instance.description = (self.data['description'], instance.description)[self.data.get('description', None) is None]        
        instance.title = (self.data['title'], instance.title)[self.data.get('title', None) is None]
        instance.save()
        return instance

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
    username = serializers.CharField(source='user.username')
    #phone_number = serializers.IntegerField()
    
    class Meta:
        model = Profile
        fields = ['user', 'description', 'phone_number','linkedin_id','github_id','twitter_id','isAuthor','account_number','total_earnings','skills_set', 'username']
        extra_kwargs = {'skills': {'required': False}, 'user': {'required': False}, 'username': {'required': False}}
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
    project_slug = serializers.CharField(source='link_to.slug', required = False)
    class Meta:
        model = Chapter
        fields = ['slug', 'project_slug', 'heading']
        extra_kwargs = { 'project_slug' : {'required': False}, 'heading':{'required': False}}
    
    def save_or_create(self, project_instance, data):
        if 'pk' in data.keys():
            for i in range(1):
                #chapter_instance.heading =  (data['chapters[' + i + ']heading'], chapter_instance.heading)[data.get('heading') is None],
                chapter_instance.heading = data['chapters[' + str(i) + '][heading]']
                chapter_instance.description = data['chapters[' + str(i) + '][description]']
                chapter_instance.content = data['chapters[' + str(i) + '][content]']
                chapter_instance.youtube_link = data['chapters[' + str(i) + '][youtube_link]']
                chapter_instance.save()
                return chapter_instance
        
        

                #chapter_instance.description =  (data['description'], chapter_instance.description)[data.get('description') is None],
                #chapter_instance.content =  (data['content'], chapter_instance.content)[data.get('content') is None],
                #chapter_instance.youtube_link =  (data['youtube_link'], chapter_instance.youtube_link)[data.get('youtube_link') is None],
            

    #def update(self, validated_data, chapter_instance, project_instance):
    ##    chapter_instance.heading =  (validated_data['heading'], chapter_instance.heading)[validated_data.get('heading') is None],
     #   chapter_instance.description =  (validated_data['description'], chapter_instance.description)[validated_data.get('description') is None],
     #   chapter_instance.content =  (validated_data['content'], chapter_instance.content)[validated_data.get('content') is None],
     #   chapter_instance.youtube_link =  (validated_data['youtube_link'], chapter_instance.youtube_link)[validated_data.get('youtube_link') is None],
     #2   #author = chapter_instance.author
     #   chapter_instance.link_to = project_instance
    #
        
        
