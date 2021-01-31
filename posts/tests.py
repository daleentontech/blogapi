from django.test import TestCase
from django.contrib.auth.models import
from .models import Post
# Create your tests here.


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create a User
        testuser1 = User.objects.create_user(
            username='testuser1',
            password='abc123'
        )
        testuser1.save()

        #create a blog post
        test_post = Post.objects.create(
            author=testuser1,
            title='Blog title',
            body='Blog Content...'
        )
        test_post.save()
