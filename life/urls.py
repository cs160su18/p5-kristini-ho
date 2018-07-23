from django.urls import path, include
from life.models import *
from . import views

urlpatterns = [
   
    # x/ means in the URL it will end in /life/x/
    # views.x calls function x in views.py
    # not sure what name does
  
    path('', views.index, name='index'),
    path('ecousers/',views.ecousers, name='ecousers'), 
    path('input/',views.ecoactions, name='ecoactions'), 
    path('output/',views.output, name='output'), 
    path('accounts/', include('django.contrib.auth.urls')),
  
#       These URLS are included with auth   
#       accounts/login/ [name='login']
#       accounts/logout/ [name='logout']
#       accounts/password_change/ [name='password_change']
#       accounts/password_change/done/ [name='password_change_done']
#       accounts/password_reset/ [name='password_reset']
#       accounts/password_reset/done/ [name='password_reset_done']
#       accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#       accounts/reset/done/ [name='password_reset_complete']

]
