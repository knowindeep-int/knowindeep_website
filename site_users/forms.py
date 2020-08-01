from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
            super(CreateUserForm,self).__init__(*args,**kwargs)
           # self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'})
           # self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'})
            # self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Password'})
            # self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Confirm Password'})
            # self.fields['email'].widget = forms.PasswordInput(attrs={'placeholder':'Email'})
            # self.fields['username'].widget = forms.PasswordInput(attrs={'placeholder':'Username'})

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        # widgets = {
        #     'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        #     'username' : forms.TextInput(attrs={'class':'form-control','placeholder':'Username'})
        # }

        