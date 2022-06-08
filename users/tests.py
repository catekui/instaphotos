from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        """creation of profile for testing
        """
        user = User.objects.create(
            username = 'moringa',
            first_name = 'sweet',
            last_name = 'cate')
        
        Profile.objects.create(
            bio = 'Back end developer',
            profile_photo = 'media/profile_pics/horse.jpeg',
            user_id = user.id
        )

    
    def test_bio(self):
        """tests the profiles bio
        """
        profile=Profile.objects.get(bio="Back end developer")
        self.assertEqual(profile.bio, "Back end developer")
        

