from django.shortcuts import render
from community.forms import *

from django.http import HttpResponse, HttpResponseRedirect
from .models import Student,Poll,Choice

import datetime
from django.db.models import Sum

# Create your views here.


def write(request):
    if request.method == 'POST':
        form =Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
    return render(request, 'write.html', {'form':form})

def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList})

def view(request, num="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html',{'article':article})


"""
"""
def first(request):
    return render(request, 'first_page.html',{})

def index(request):
    students = Student.objects.all()
    context = {'students':students}
    return render(request, 'team/index.html',context)

def assignments(request):
    assignments = Assignment.objects.all()
    context = {'assignments':assignments}
    return render(request, 'assessment.html',context)


def areas(request, party_number) : #어떤 지역인지를 매개변수 area로 받습니다.

    students = Student.objects.filter(party_number = party_number)
    #Candidate의 area와 매개변수 area가 같은 객체만 불러오기

    context = {'students':students,
    'party_number':party_number}
    return render(request,'team/area.html',context)

"""
def polls(request, poll_id):
    poll = Poll.objects.get(pk = poll_id)
    selection = request.POST['choice']
    try:
        choice = Choice.objects.get(poll_id = poll.id, student_id = selection)
        choice.votes += 1
        choice.save()
    except:
        #최초로 투표하는 경우, DB에 저장된 Choice객체가 없기 때문에 Choice를 새로 생성합니다
        choice = Choice(poll_id = poll.id, student_id = selection, votes = 1)
        choice.save()
    return HttpResponseRedirect("/areas/{}/results".format(poll.area))

def results(request, area):
    students = Student.objects.filter(area = area)
    polls = Poll.objects.filter(area = area)
    poll_results = []
    for poll in polls:
        result = {}
        result['start_date'] = poll.start_date
        result['end_date'] = poll.end_date
        total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))
        result['total_votes'] = total_votes['votes__sum']
        rates = []
        for student in students:
            try:
                choice = Choice.objects.get(poll_id = poll.id,
                student_id = student.id)
                rates.append(round(choice.votes*100/result['total_votes'],2))
            except:
                rates.append(0)
        result['rates'] = rates
        poll_results.append(result)

    context = {'students':students, 'area':area,
    'poll_results' : poll_results}
    return render(request, 'team/result.html', context)
"""
