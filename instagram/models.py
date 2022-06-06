from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images',null=True,blank="True")
    image_name = models.CharField(max_length=100)
    image_caption = models.TextField(max_length=1000)
    image = CloudinaryField('image')
    profile = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank="True")
    likes_number = models.IntegerField(default=0)
    comments_number = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1200, null=True, blank=True)
    profile_photo = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment