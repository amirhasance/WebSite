from django.db import models
from django.contrib.auth.models import User

class Video (models.Model):
    
    caption = models.CharField(max_length = 200)
    videoFile = models.FileField(upload_to='./videos')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    likes = models.IntegerField()
    date = models.DateTimeField()
    
    def comments(self):
        comments = Post.objects.filter(video = self)
        return comments
    
    def __str__(self):
        return "{}  ,  {} ".format(self.caption , self.videoFile)

class Post_Video(models.Model):
    
    video = models.ForeignKey(Video, on_delete=models.CASCADE  )
    description = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField()
    
    
    def __str__(self):
        return "\n{} :: {}".format(self.title , self.comment)
    
    
    