from django.forms import ModelForm , Form
from .models import Comment
from django import forms

class Comment_Form(ModelForm):
  
  class Meta:
    model = Comment
    fields = ['comment']
    
class Commentt(Form):
 
  name = forms.CharField(max_length=3 , required=True  )
  Image = forms.ImageField()
  file = forms.FileField()
  
