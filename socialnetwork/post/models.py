from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User , related_name = 'post' , on_delete = models.CASCADE)
    title = models.CharField(max_length = 256)
    post_picture = models.ImageField(upload_to = 'pictures/%Y/%m/%D/' ,null = True,blank = True, width_field = "width_field" , height_field = "height_field", max_length = 256)
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)
    caption = models.TextField(max_length = 256)
    like = models.ManyToManyField(User , related_name = 'likes')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail' , kwargs = {'pk': self.pk} )

    def total_likes(self):
        return self.like.count()

class Comment(models.Model):
    post = models.ForeignKey(Post , null = True, related_name = 'comments' , on_delete = models.CASCADE)
    parent = models.ForeignKey('self' , null = True , related_name = 'replies' , on_delete = models.CASCADE)
    userr = models.ForeignKey(User , null = True , related_name = 'comments' , on_delete = models.CASCADE)
    comment_text = models.TextField(max_length = 256)
    commented_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        post = self.post
        return reverse('home')
