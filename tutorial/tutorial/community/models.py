from django.db import models

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    url = models.URLField()
    email = models.EmailField()
    cdate = models.DateTimeField(auto_now_add=True)



class Student(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField(default=1)
    Major = models.CharField(max_length=50)
    GPA = models.FloatField(blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Team(models.Model):
    party_number = models.ForeignKey(Student)
    party_number = models.IntegerField(default=1)
    tutor_name = models.CharField(max_length=10)
    fortnightly_meeting = models.TextField()

class Poll(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    area =models.CharField(max_length=15)

class Assignment(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    information = models.TextField()


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    student = models.ForeignKey(Student)
    votes = models.IntegerField(default=0)
