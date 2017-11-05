from django.forms import ModelForm
from community.models import *
from django import forms
from django.contrib.auth.models import User
from .models import Document


# Project data form
class Form(ModelForm):
    class Meta:
        model = Article
        fields=['name', 'title', 'contents', 'url', 'email','document']
# Project application form
class Form_Application(ModelForm):
    class Meta:
        model = Application
        fields=['name', 'team_number', 'contents', 'email','document']
# Assignment form for Student
class Form_Assignmet(ModelForm):
    class Meta:
        model = Assignment_Form
        fields=['name', 'student_number' ,'contents', 'document']

# Login Data form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['username','email','password']
#########################
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document' )



#################
