from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse , JsonResponse
from django.shortcuts import render , get_object_or_404 , redirect
from gallery.models import Token
# Create your views here.
def login(request):
  
  return JsonResponse({'message':'under construction'})

@csrf_exempt
def whoami(request):
  
  if request.method == 'POST':
   
    import pdb
    pdb.set_trace()
    if  request.POST.__contains__('token'):
      
      this_token = request.POST['token']
    
      this_user = get_object_or_404(User , token__token = this_token)
    
      return JsonResponse({'user': this_user.username})
    
  
  return HttpResponse("<body><h3>Please send Token , after that i can sat who are you</h3></body>")
  


def register():
  pass