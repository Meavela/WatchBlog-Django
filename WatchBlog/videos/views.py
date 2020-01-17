from django.shortcuts import render
from django.contrib.auth import authenticate
from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import VideoModelForm
from .models import Video

# Create your views here.
def index(request):
    template = loader.get_template('videos/index.html')
    # user = authenticate(username='Lou', password='admin')
    context = {'user': request.user}
    print(request.user.is_authenticated)
    print(request.user)
    return HttpResponse(template.render(context, request))

def list(request):
    template = loader.get_template('videos/list.html')
    all_entries = Video.objects.all()    
    context = {'videos':all_entries}

    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'POST':
        form = VideoModelForm(request.POST)

        if form.is_valid:
            form.save()
            
            return HttpResponseRedirect(reverse('list'))
    else:
        form = VideoModelForm()
    
    return render(request, 'videos/create.html', {'form':form})

def signin(request):
    template = loader.get_template('videos/signin.html')
    context = {}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('videos/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def logout(request):
    template = loader.get_template('videos/logout.html')
    context = {}
    return HttpResponse(template.render(context, request))