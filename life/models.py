from django.db import models
from django.contrib.auth.models import User

class EcoAction(models.Model):
  """ A model that connects an ecologically friendly action to its point value."""
  
  action_name = models.CharField(max_length=200)
  point_value = models.IntegerField()
  
  def __str__(self):
    return self.action_name + ' (' + str(self.point_value) + ' ' + 'pts)'

class EcoUser(User): 
  """ Extends Django's built in User model, which already has properties such as
  username and password."""
  
  eco_actions = models.ManyToManyField(EcoAction)  
  
  def __str__(self):
    return self.first_name + ' ' + self.last_name
  
  @property
  def points_earned(self):
    total_points = 0
    for action in self.eco_actions.all(): 
      total_points += action.point_value
    return total_points
  
 
