from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import Comment_Form , Commentt
from django.shortcuts import render
from .models import Comment
from django.contrib import messages
import requests
from django.shortcuts import redirect
# Create your views here.
@csrf_exempt
def home(request , template_name='home.html' ):
  comments = Comment.objects.all()
  if request.method == 'POST':
        form = Comment_Form(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': "6LdpF_EUAAAAAMd29Jx520Gp9UF5k2aplaIlpU4D",
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                form.save()
                messages.success(request, 'New comment added with success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('home')
  
  form  = Commentt()
  return render (request  , template_name , {'form':form})