from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
  comment = models.CharField(max_length=200)
  user = models.ForeignKey(User , on_delete=models.CASCADE)
  date = models.DateTimeField()
  
  def __str__(self):
    return "{}".formant(self.comment)
  
  