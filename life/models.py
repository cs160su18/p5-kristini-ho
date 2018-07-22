from django.db import models
from django.contrib.auth.models import User

class EcoAction(models.Model):
  action_name = models.CharField(max_length=200)
  point_value = models.IntegerField()
  
  def __str__(self):
    return 'Action: ' + self.action_name

class EcoUser(User): # extend Django's built in User model, which already has username + password
  eco_actions = models.ManyToManyField(EcoAction)
  points_earned = eco_actions.count * 10 # TO DO: figure out how to calculate on the fly...
    
