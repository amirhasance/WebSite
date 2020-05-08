from django.shortcuts import render
from django.forms import ModelForm
from django.shortcuts import render , redirect , get_object_or_404
from .models import Video
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt , ensure_csrf_cookie
from django import forms 
from django.contrib.auth.models import User
# //// video_update
# /// video_delete
# /// video_new
# /// home

class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields =  "__all__"
# this is just is form and template of data when receiving ,,, 
# it is import when we use a class in models to save data posted

class test_VideoForm(forms.Form):
    
    def __init__(self , *args , **kwargs):
        super(test_VideoForm  , self ).__init__(*args )
        
        # if kwargs :
            
        #  if dict(list(kwargs.items())).__contains__('items'):
        #     for x in dict(list(kwargs.items()))['items'] :
        #        print(x)
        print(kwargs)

    name = forms.CharField(required=True , )
    video = forms.FileField(required = True )

class Video_Form1(forms.Form):
    caption = forms.CharField(max_length=200)
    video = forms.FileField();



class post_Form(forms.Form):
    title = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=300)
    
# #    def __init__(self , *args , **kwargs):
#     #    super.__init__()
#        name = forms.CharField(max_length=5)
#        image = forms.ImageField()
#        video = forms.FileField()
#     #    super().__init__(*args , **kwargs)
def  home(request , template_name='video/home.html' ):
    vidoes = Video.objects.all()
    data = {}
    data['videos'] = vidoes
    return render(request ,template_name  , data)
    # return HttpResponse()
def video_new(request , template_name='video/form.html'):
    print(request.POST)
    form = Video_Form1(request.POST or None , request.FILES or None)
    if form.is_valid():
        caption = form.cleaned_data.get('caption')
        video = form.cleaned_data.get('video')
        user = User.objects.get(pk = 7)
        from datetime import datetime
        new_video = Video.objects.create(caption=caption , videoFile = video , user=user , likes = 0 ,date = datetime.now() )
        return redirect('video:home')
    data = {}
    data['form'] = form
    return render(request ,template_name ,data )
    # return HttpResponse("<body><p> this is paragraph</p></body>")
def video_update(request ,pk , template_name='form.html'):
    video = get_object_or_404(video , pk=pk)
    
    form = VideoForm(request.POST or None , instance=video)
    if form.is_valid():
        form.save()
        return redirect('video:home')
    return render(request , template_name , {'form' , form})
def video_delete(request , pk , template_name='confirm.html'):
    video = get_object_or_404(video , pk=pk)
    if request.method=='POST':
        video.delete()
        return redirect('video:home')
    return render(request  , template_name , {'object':video})

from .models import Post_Video
@csrf_exempt
def post(request, template_name='post_comment.html'  , pk =None):
    
    if request.method == "POST":
        print(request.POST)
        form = post_Form(request.POST or None)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            comment = form.cleaned_data.get('comment')
            Post.objects.create(title=title , comment=comment , video = pk)
        else :
            print('Not Valiiiiiiiiiiiiiiiiiiiiiiiid')
    else :
        data = {}
        form = post_Form()
        data['form'] = form
        return render(request ,template_name, data)
            
            

@csrf_exempt
def test_function(request , template_name='test.html' ):
    # for x in Video.objects.all():
    #     print(x)
    data = {}
    if request.method == 'POST':
        form = test_VideoForm(request.POST or None , request.FILES or None  , )
        if form.is_valid():
            name = form.cleaned_data.get('name')
            video = form.cleaned_data.get('video')
            # if not Video.objects.__contains__(name=name , video=video):
            #     Video.objects.create(name=name , video = video)
            # else :
            #     pass
            new_video = Video.objects.create(videoName = name , videoFile = video)  
            print("Success")
            return HttpResponse("OK")
            
    form = test_VideoForm()
    data['form'] = form
    return render (request , template_name , data)


    
#   form  = test_VideoForm(request.POST , items = Video.objects.all())
#   if form.is_valid():
#       form.save()
#       print("Successssssssssss")

  
#   return render(request , template_name , {'form' : form} )

    


  
