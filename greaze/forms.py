from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class InstaRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username','password1','password2' ]

        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'last_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Second Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password1':forms.PasswordInput(attrs = {'class':'form-control ','type':'password', 'placeholder':"Password", 'label': 'Password'}),
            'password2':forms.PasswordInput(attrs = {'class':'form-control', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }

class PostProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','image','description','profile']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Project Title...'}),
            'image':forms.TextInput(attrs={'class':'form-control names','placeholder':'In a word...','label':'Put a name'}),
            'description':forms.Textarea(attrs={'class':'form-control names','placeholder':"Caption",'label':"Caption"}),
        }

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['design','usability','content']

        widgets = {
            'design': forms.SelectMultiple(attrs={'class':'form-control','name':'design'}),
            'usability': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Input value','name':'usability'}),
            'content': forms.SelectMultiple(attrs={'class':'form-control','name':'content'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo','bio']

        widgets = {
            'profile_photo':forms.FileInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control names','placeholder':'Write here...','label':'Put a name'}),
        }