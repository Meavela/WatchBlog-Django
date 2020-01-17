from django.shortcuts import render
from django.contrib.auth import authenticate
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

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
    context = {}
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('videos/create.html')
    context = {}
    return HttpResponse(template.render(context, request))