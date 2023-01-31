from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.template import loader
from django.http import HttpResponse, request
from .forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    if request.user.is_authenticated:
        notice = Notice.objects.all()
        attendance = Attendance.objects.all()
        marks = Marks.objects.all()

        template = loader.get_template('home.html')
        context = {
            'notice': notice,
            'marks': marks,
            'attendance': attendance,
        }
        return HttpResponse(template.render(context, request))
    else:
        template=loader.get_template('Welcome.html')
        context={}
        return HttpResponse(template.render(context,request))


def addAttendance(request):
    if request.user.is_authenticated:
        form = addAttendanceForm()
        if (request.method == 'POST'):
            form = addAttendanceForm(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('home')
        addAttendanceTemplate = loader.get_template('AddAttendance.html')
        context = {'form': form}
        return HttpResponse(addAttendanceTemplate.render(context,request))
    else:
        return redirect('home')

def addMarks(request):
    if request.user.is_authenticated:
        form = addMarksForm()
        if (request.method == 'POST'):
            form = addMarksForm(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('home')
        addMarksTemplate=loader.get_template('AddMarks.html')
        context = {'form': form}
        return HttpResponse(addMarksTemplate.render(context,request))
    else:
        return redirect('home')

def addNotice(request):
    if request.user.is_authenticated:
        form = addNoticeForm()
        if (request.method == 'POST'):
            form = addNoticeForm(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('home')
        addNoticeTemplate=loader.get_template('AddNotice.html')
        context = {'form': form}
        return HttpResponse(addNoticeTemplate.render(context,request))
    else:
        return redirect('home')
@csrf_protect

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        registerTemplate = loader.get_template('Register.html')
        form=UserCreationForm()

        if request.method=='POST':
            form=UserCreationForm(request.POST)
            if form.is_valid():
                user=form.save()
                return redirect('login')

        context={
                'form':form,
            }
        return HttpResponse(registerTemplate.render(context,request))
@csrf_protect

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        loginTemplate = loader.get_template('Login.html')
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')

    context={

    }
    return HttpResponse(loginTemplate.render(context,request))

def logoutPage(request):
    logout(request)
    return redirect('login')