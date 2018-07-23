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
  current_user = request.user
  name = current_user.first_name + ' ' + current_user.last_name
  eco_user = EcoUser.objects.filter(user=current_user)[0]
  eco_actions = eco_user.eco_actions.all()
  points = str(eco_user.points_earned)
  return render(request, 'life/output.html', {"name": name, "points": points, "currentuser": current_user, "ecoactions": eco_actions})



