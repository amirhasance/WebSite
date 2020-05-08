from django.db import models

# Create your models here.
from django.contrib.auth.models import User


import hashlib

def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

class my_users(User):
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # self.password = hash_string(self.password)
  
  # def __eq__(self, other):
  #   return super().__eq__(other) or self.password == hash_string(other.password)
  
  def __str__(self):
    return f'{self.username} : {self.password}'