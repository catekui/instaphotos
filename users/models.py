from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=400,blank=True,null=True)
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.save()
        
    def update(self):
        self.save()
    

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 280 or img.width > 280:
    #         output_size = (280, 280)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)