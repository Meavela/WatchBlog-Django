from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .forms import VideoModelForm, UserForm, LoginForm
from .models import Video
import time

# Create your views here.
def index(request):
    template = loader.get_template('videos/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def list(request):
    template = loader.get_template('videos/list.html')
    all_entries = Video.objects.all()    
    context = {'videos':all_entries}

    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'POST':
        form = VideoModelForm(request.POST, request.FILES)

        if form.is_valid():
            rate = form.cleaned_data['rate']
            form.save()

            return HttpResponseRedirect(reverse('list'))
    else:
        form = VideoModelForm()
    
    return render(request, 'videos/create.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(username,email,password)
            user.last_name = last_name
            user.first_name = first_name
            user.save()

            return HttpResponseRedirect(reverse('login'))

    else:
        form = UserForm()
    
    return render(request, 'videos/signin.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))

    else:
        form = LoginForm()
    
    return render(request, 'videos/login.html', {'form':form})

def logout_view(request):
    logout(request)

    return HttpResponseRedirect(reverse('index'))

def detail(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404
    template = loader.get_template('videos/detail.html')
    context = {'video': video}
    return HttpResponse(template.render(context, request))

def edit(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = VideoModelForm(request.POST, request.FILES, instance=video)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list'))
    
    else:
        form = VideoModelForm(instance=video)
    
    return render(request, 'videos/edit.html', {'form':form})

def delete(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        raise Http404
    template = loader.get_template('videos/delete.html')
    context = {'video': video}
    if request.method == 'POST':
        video.delete()
        return HttpResponseRedirect(reverse('list'))

    return HttpResponse(template.render(context, request))
