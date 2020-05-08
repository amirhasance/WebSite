from django.urls import path 

from . import views

app_name='video'

urlpatterns = [
    
    path(''  , views.home , name='home' ),
    
    path('new/' , views.video_new , name='video_new'),
    
    path('edit/<int:pk>' , views.video_update  , name='video_update'),
    
    path('delete/<int:pk>' , views.video_delete , name='video_delete'),
    
    path('test/' , views.test_function   , name='video_test'),
    
    path('post/' , views.post , name = 'video_post')
]
