import os
from django.http.response import HttpResponse
from covid_awareness.settings import BASE_DIR
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.conf import settings
from .models import ProfileImage,QuestionSurvey
from .forms import ImageForm
# Create your views here.
def hospital_detail(request):
    return render(request,'hospital_detail.html',{})
def homepage(request):
    print(BASE_DIR)
    if request.method=="POST":
        username = ''
        for x in request.POST['email']:
            if x == '@':
                break
            username += x
        password = request.POST['pass']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request,'login.html',{"msg":True})   
    
    return render(request,'index.html',{})
def signup(request):
    form = ImageForm()
    return render(request,'signup.html',{'form':form})
def signin(request):
    if request.method == "POST":
        username = ''
        for x in request.POST['email']:
            if x == '@':
                break
            username += x
        user = User.objects.create_user(
            username,
            request.POST['email'],
            request.POST['pass1']
        )
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            p = ProfileImage.objects.all()
            os.rename(os.path.join(BASE_DIR,(p[len(p)-1].image.url)[1:]),os.path.join(BASE_DIR,"media/images/"+request.POST['email']+os.path.splitext(p[len(p)-1].image.url)[1]))
    return render(request,'login.html',{})
def symtoms_analysis(request):
    if request.method == "POST":
        qs = QuestionSurvey(
            q1= True if request.POST['q1']=='Yes' else False,
            q2= True if request.POST['q2']=='Yes' else False,
            q3= True if request.POST['q3']=='Yes' else False,
            q4= True if request.POST['q4']=='Yes' else False,
        )
        count = 4
        for x in request.POST.values():
            if x == "No":
                count -= 1

        qs.save()
        return render(request,'show_info.html',{'count':count})
    return render(request,'symptom_analysis.html',{})
def signout(request):
    logout(request)
    return render(request,'index.html',{})
def profile(request):
    p = os.listdir(os.path.join(BASE_DIR,'media/images'))
    filename = ''
    for file in p:
        if file.find(request.user.email)!=-1:
            filename = file
            break
    return render(request,'user_profile.html',{'filename':filename})