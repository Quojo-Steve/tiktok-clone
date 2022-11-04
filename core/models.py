from .validators import file_size
from django.db import models
import uuid
from datetime import datetime


class VideoUpload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100, default="user")
    description = models.TextField(max_length=50)
    post_date = models.DateTimeField(default = datetime.now)
    video = models.FileField(upload_to="videos", blank=False, validators=[file_size])
    no_of_likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user


class Likes(models.Model):
    video_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username +"likes this post"
    

class Followers(models.Model):
    logged_in_user = models.CharField(max_length = 100)
    follow = models.CharField(max_length=100)
    
    def __str__(self):
        return self.logged_in_user
