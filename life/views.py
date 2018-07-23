from django.shortcuts import render
from django.core import serializers
from django.contrib.auth import authenticate, login
from life.models import *

def index(request):
  return render(request, 'life/index.html', {})

def ecousers(request):
  all_users = EcoUser.objects.all()
  return render(request, 'life/index.html', {"ecousers": all_users})

def ecoactions(request):
  all_actions = EcoAction.objects.all()
  return render(request, 'life/input.html', {"ecoactions": all_actions})

def login(request):
  return render(request, 'life/accounts/login.html', {}, RequestContext(request))

def output(request):
  return render(request, 'life/output.html', {})


