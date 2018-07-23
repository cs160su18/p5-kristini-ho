from django.db import models
from django.contrib.auth.models import User

class EcoAction(models.Model):
  """ A model that connects an ecologically friendly action to its point value."""
  
  action_name = models.CharField(max_length=200)
  point_value = models.IntegerField()
  
  def __str__(self):
    return self.action_name + ' (' + str(self.point_value) + ' ' + 'pts)'

class EcoUser(models.Model): 
  """ Connected to Django's User model, which already has properties such as
  username and password."""
  
  eco_actions = models.ManyToManyField(EcoAction)  
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return 'username: ' + self.user.username + ', name: ' + self.user.first_name + ' ' + self.user.last_name
  
  @property
  def points_earned(self):
    total_points = 0
    for action in self.eco_actions.all(): 
      total_points += action.point_value
    return total_points
  
 
