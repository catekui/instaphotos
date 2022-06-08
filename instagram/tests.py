from django.test import TestCase
from .models import *
from users.models import Profile

# Create your tests here.

class ImageTestCase(TestCase):
    def setUp(self):
        """image creation
        """
        user = User.objects.create(
            username = 'Moringa',
            first_name = 'Sweet',
            last_name = 'Cate')
        
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
            username = 'Moringa',
            first_name = 'Sweet',
            last_name = 'Cate')
         
         Profile.objects.create(
            bio = 'me',
            profile_photo = 'media/profile_pics/horse.jpeg',
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
            username = 'Moringa',
            first_name = 'Sweet',
            last_name = 'Cate')
         
         Image.objects.create(
            name="me",
            caption="ooops",
            profile_id=user.id,
            user_id=user.id
        )