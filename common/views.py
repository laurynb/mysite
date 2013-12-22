from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from datetime import *
#from app.forms import *
from common.models import *

def home(request):
   context = {}
   return render(request, 'mysite/common/index.html', context)

def about(request):
   context = {}
   return render(request, 'mysite/common/about.html', context)

def projects(request):
   context = {}
   return render(request, 'mysite/common/projects.html', context)

def blog(request):
   context = {}
   return render(request, 'mysite/common/blog.html', context)

def contact(request):
   context = {}
   return render(request, 'mysite/common/contact.html', context)
