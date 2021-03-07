from rest_framework import fields, serializers

from blogs.models import Project, Comment, Profile, Language, Chapter, Suggestion

class ProjectSerializer(serializers.ModelSerializer):
    title = serializers.CharField(allow_blank=True, allow_null=True, required = False, max_length = 25)
    class Meta:
        model = Project
        #fields = ['topic','topic_image','topic_content']
        fields = ['image', 'title', 'slug', 'overview', 'languages','difficulty_level','no_of_hours','pre_req']
        extra_kwargs = {'slug': {'required': False}, 'title': {'required': False}}

    def update(self, instance, data):
        #instance.description = (data['description'], instance.description)[data.get('description', None) is None]        
        if 'description' in data:
            instance.description = (data['description'], instance.description)[data['description'] is None]
        instance.title = (self.data['title'], instance.title)[self.data.get('title', None) is None]
        #instance.image = (self.data['image'], instance.image)[self.data.get('image', None) is None]
        #print(self.data.image)
        if 'image' in data:
            instance.image = (data['image'], instance.image)[data['image'] is None]
        instance.overview =(self.data['overview'], instance.overview)[self.data.get('overview', None) is None]
        instance.difficulty_level =(self.data['difficulty_level'], instance.difficulty_level)[self.data.get('difficulty_level', None) is None]
        instance.no_of_hours =(self.data['no_of_hours'], instance.no_of_hours)[self.data.get('no_of_hours', None) is None]
        if 'pre_req' in data:
            instance.pre_req =(self.data['pre_req'], instance.pre_req)[self.data.get('pre_req', None) is None]
        if dict(data).get('languages[]'):
            if data['isAdded'] == 'false':
                instance.languages.clear()
            for language in dict(data).get('languages[]'):
                
                try:
                    language_obj = Language.objects.get(name__iexact = language)
                except Language.DoesNotExist:
                    language_obj = Language.objects.create(name = language.capitalize())

                instance.languages.add(language_obj)

        # if dict(data).get('pre_req[]'):
        #     if data['isAdded'] == 'false':
        #         instance.pre_req.clear()
        #     for pre_req in dict(data).get('pre_req[]'):
        #         try:
        #             pre_req_obj = PreRequisite.objects.get(name__iexact = pre_req)
        #         except PreRequisite.DoesNotExist:
        #             pre_req_obj = PreRequisite.objects.create(name = pre_req.capitalize())

        #         instance.pre_req.add(pre_req_obj)
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
        fields = '__all__'
    
    def update(self, chapter_instance):
        print(self.validated_data)
        # print(chapter_instance.title)
        chapter_instance.content =  (self.validated_data['content'], chapter_instance.content)[self.validated_data.get('content') is None]
        chapter_instance.title =  (self.validated_data['title'], chapter_instance.title)[self.validated_data.get('title') is None]
        chapter_instance.save()
        #extra_kwargs = { 'link_to' : {'required': False}, 'heading':{'required': False}, 'id': {'read_only':True}}            

    #def update(self, validated_data, chapter_instance, project_instance):
    ##    chapter_instance.heading =  (validated_data['heading'], chapter_instance.heading)[validated_data.get('heading') is None],
     #   chapter_instance.description =  (validated_data['description'], chapter_instance.description)[validated_data.get('description') is None],
     #   chapter_instance.content =  (validated_data['content'], chapter_instance.content)[validated_data.get('content') is None],
     #   chapter_instance.youtube_link =  (validated_data['youtube_link'], chapter_instance.youtube_link)[validated_data.get('youtube_link') is None],
     #2   #author = chapter_instance.author
     #   chapter_instance.link_to = project_instance
    #
        
class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = "__all__"
