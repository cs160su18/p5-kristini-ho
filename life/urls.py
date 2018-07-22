from django.urls import path
from life.models import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # views.ecousers is the function from views.py that gets called
    # http://p5-kristini-ho-kristinho836388.codeanyapp.com:8000/life/ecousers/
    path('ecousers/',views.ecousers, name='ecousers'), 
    path('input/',views.ecoactions, name='ecoactions'), 

]
