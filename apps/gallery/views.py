from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse , JsonResponse
from django.forms import ModelForm
from gallery.models import Image
from .serializer import ImageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django import forms
from django.contrib.auth.models import User
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image' , 'caption' ]
class Image_Form1(forms.Form):
    caption = forms.CharField(max_length=30)
    image = forms.ImageField()
    
@csrf_exempt 
def react(request):
   if request.method == "GET":
       serializer = ImageSerializer(Image.objects.all() , many=True)
       print('//////////////////////////////////////////')
    #    return Response({'message' : 'its wroking'} , status=status.HTTP_200_OK)
       return JsonResponse({'message' : 'its working' , 'data': serializer.data})
       
       

def index(request, template_name='gallery/index.html'):
    images = Image.objects.all()
    # print(request.session['name'])
    
    data = {}
    data['object_list'] = images

    return render(request, template_name, data)

from datetime import datetime

def image_create(request, template_name='gallery/form.html'):
    form = Image_Form1(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            
            caption = form.cleaned_data.get("caption")
            image = form.cleaned_data.get('image')
            user = User.objects.get(pk=7)
            img = Image.objects.create(caption = caption , image =image , user=user, date =datetime.now() , likes=0)
            return redirect('gallery:home')
    return render(request, template_name, {'form':form})    

def image_update(request, pk, template_name='gallery/form.html'):
    image = get_object_or_404(Image, pk=pk)
    form = ImageForm(request.POST or None, instance=image)
    if form.is_valid():
        form.save()
        return redirect('gallery:home')
    return render(request, template_name, {'form':form})

def image_delete(request, pk, template_name='gallery/confirm_delete.html'):
    image = get_object_or_404(Image, pk=pk)    
    if request.method=='POST':
        image.delete()
        return redirect('gallery:home')
    return render(request, template_name, {'object':image})    
def IncreamentLike(request , pk):
    image = get_object_or_404(Image , pk=pk)
    if request.method == 'POST':
        image.Increament_like
        return
    else:
        return JsonResponse({'message':'GET‌ is not Allowed'})
    
        
    