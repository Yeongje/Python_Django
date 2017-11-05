from django.db import models


#file?
from django.core.urlresolvers import reverse
# Create your models here.


################
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

##################

# project
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
# project apllication
class Application(models.Model):
    name = models.CharField(max_length=50)
    team_number = models.CharField(max_length=50)
    contents = models.TextField()
    email = models.EmailField()
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
# assignment submittion
class Assignment_Form(models.Model):
    name = models.CharField(max_length=50)
    student_number = models.CharField(max_length=50)
    contents = models.TextField()
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# student
class Student(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    party_number = models.IntegerField(default=1)
    Major = models.CharField(max_length=50)
    GPA = models.FloatField(blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name
# team
class Team(models.Model):
    party_number = models.ForeignKey(Student) #studnet move later
    party_number = models.IntegerField(default=1)
    tutor_name = models.CharField(max_length=10)
    fortnightly_meeting = models.TextField()

# assignment - admin part
class Assignment(models.Model):
    assignment_name = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    information = models.TextField()
    assignment_file = models.FileField()
# tutor
class Tutor(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
    assigned_team = models.ForeignKey(Team)
# Unit_Coordinator
class Unit_Coordinator(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
# Supervisor
class Project_Supervisor(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField()
