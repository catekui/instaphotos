from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT,related_name='user_images')
    image = models.ImageField(upload_to = 'media/', null = True, blank = True)
    name = models.CharField(max_length=40)
    caption = models.CharField(max_length=200)
    posted_on = models.DateTimeField(auto_now_add=True)
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    comment = models.IntegerField(blank=True,null=True,default=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    
    
    class meta:
        ordering =['posted_on']
        
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
        
    @classmethod
    def search_by_name(cls,search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts
    
    @property
    def saved_comments(self):
        return self.comments.all()
    
    @property
    def saved_likes(self):
      return self.postslikes.count()
    
    def __str__(self):
        return self.name
    
reactions={('Like','Like'),('Unlike','Unlike')}
        
        

class Comment(models.Model):
    comment = models.CharField(max_length=300)
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')
    
    
    @classmethod
    def display_comment(cls,image_id):
        comments = cls.objects.filter(image_id = image_id)
        return comments
    
class Like(models.Model):
    response = models.CharField(choices=reactions,default='like',max_length=70)
    image = models.ForeignKey(Image,on_delete = models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.response