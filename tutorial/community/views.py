from django.shortcuts import render, redirect #redirect login
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout #login
from django.views.generic import View #login
from .forms import UserForm, DocumentForm # login,fileupload
from community.forms import *

from django.http import HttpResponse, HttpResponseRedirect
from .models import Student,Document

import datetime
from django.db.models import Sum



# Imaginary function to handle an uploaded file.
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#########################################
def download(request):
    documents = Document.objects.all()
    return render(request, 'download.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })

######################################3

#Write project
def write(request):
#    if request.method == 'POST':
#        form =Form(request.POST)
#        if form.is_valid():
#            form.save()
#    else:
#        form = Form()

    if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Form()
    return render(request, 'write.html', {
        'form': form
    })

#    return render(request, 'write.html', {'form':form})

def write_application(request):
    if request.method == 'POST':
        form = Form_Application(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Form_Application()
    return render(request, 'apply_project.html', {
        'form': form
    })

def sumbit_assignmet(request):
    if request.method == 'POST':
        form = Form_Assignmet(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Form_Assignmet()
    return render(request, 'submit_assignment.html', {
        'form': form
    })

def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList})

def view(request, num="1"):
    article = Article.objects.get(id=num)
    documents = Document.objects.all()
    context = {'article':article, 'documents': documents }
    #return render(request, 'view.html',{'article':article})
    return render(request, 'view.html',context)


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

def assessment_infor(request):
    assignments = Assignment.objects.all()
    context = {'assignments':assignments}
    return render(request, 'assessment_infor.html',context)

def teams(request, party_number) :
    students = Student.objects.filter(party_number = party_number)
    context = {'students':students, 'party_number':party_number}
    return render(request,'team/group.html',context)




#login
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'team/index.html', {'students': students})

    return render(request, 'login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'team/index.html', {'students': students})
    context = {
        "form": form,
    }
    return render(request, 'registration_form.html', context)

#file uploaded
