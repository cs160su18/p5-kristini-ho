from django.urls import path
from life.models import *
from . import views

urlpatterns = [
  
    # views.x calls function x in views.py
    # x/ means in the URL it will end in /life/x/
    # not sure what name does
  
    path('', views.index, name='index'),
    path('ecousers/',views.ecousers, name='ecousers'), 
    path('input/',views.ecoactions, name='ecoactions'), 
    path('login/',views.login_page, name='login'), 
    path('output/',views.output, name='output'), 

]
