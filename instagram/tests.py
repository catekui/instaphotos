from django.test import TestCase
from .models import *
from users.models import Profile

# Create your tests here.

class ImageTestCase(TestCase):
    def setUp(self):
        """image creation
        """
        user = User.objects.create(
            username = 'nashlil',
            first_name = 'lilian',
            last_name = 'kanana')
        
        Image.objects.create(
            name="me",
            caption="ooops",
            profile_id=user.id,
            user_id=user.id
        )
    def test_image_name(self):
        """tests image name
        """
        image=Image.objects.get(name="me")
        self.assertEqual(image.name, "me")


class LikeTestCase(TestCase):
    def setUp(self):
         user = User.objects.create(
            username = 'Lucy',
            first_name = 'Mutanu',
            last_name = 'Kioko')
         
         Profile.objects.create(
            bio = 'me',
            profile_photo = 'media/profile_pics/pizzacart10-removebg-preview_edhHkdQ.png',
            user_id = user.id
        )
        
         Image.objects.create(
            name="me",
            caption="ooops",
            profile_id=user.id,
            user_id=user.id
        )


def test_image_id(self):
         user = User.objects.create(
            username = 'nashlil',
            first_name = 'lilian',
            last_name = 'kanana')
         
         Image.objects.create(
            name="me",
            caption="ooops",
            profile_id=user.id,
            user_id=user.id
        )