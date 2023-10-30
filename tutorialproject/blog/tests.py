from django.test import TestCase
from .models import Post
class YourTestClass(TestCase):

    

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data             for all class methods.")
        
        pass


    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass
      
    def test_name_label(self):
        posts = Post.objects.all()
        for post in posts:
          print(post)
        self.assertEqual(posts, Post)
        