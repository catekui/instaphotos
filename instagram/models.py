from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1200, null=True, blank=True)
    profile_photo = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.image_name