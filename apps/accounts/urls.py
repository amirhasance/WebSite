
from django.urls import path 

from . import views


urlpatterns = [
    # url(r'^accounts/register/?$', views.register, name='register'),
    # url(r'^accounts/whoami/?$', views.whoami, name='whoami'),
    # url(r'^accounts/login/?$', views.login, name='login'),
    
    path('' , views.login , name='login'),
    path('login/' , views.login , name='login'),
    path('register/' , views.register , name = 'register'),
    path('whoami/' , views.whoami , name='whoami'),
    
]
