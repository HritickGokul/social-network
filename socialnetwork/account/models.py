from django.db import models
from django.contrib.auth.models import User , PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name = 'profile' ,  on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length = 150 , null = True)
    slug = models.SlugField(allow_unicode=True, unique=True , null = True)
    followers = models.ManyToManyField(User , related_name = 'followers')
    following = models.ManyToManyField(User , related_name = 'following')

    def save(self , *args , **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args , **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save , sender = User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)
