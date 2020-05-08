from django.db import models
from django.contrib.auth.models import User
class Image(models.Model):
    caption = models.CharField(max_length=30)
    image = models.ImageField(upload_to='gallery')
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField()
    likes = models.IntegerField()

    def __str__(self):
        return "name: %s and image :‌%s" % (self.caption, self.image)
    def Increament_like(self):
        self.likes +=1
        self.save()
    
    
class Post_Image (models.Model):
    
    image = models.ForeignKey(Image , on_delete=models.CASCADE  )
    description = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField()
    
    def __str__(self):
        return "{}".format(self.description)
    
    def IncreaseLike(self):
        self.likes +=1
    
class Token (models.Model):
    token = models.CharField(max_length= 200)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".fromat(self.user.username)