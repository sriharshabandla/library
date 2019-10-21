from django.db import models
from django.test import TestCase
from .models import Author

# Create your tests here.

class TestBook(TestCase):
    def setUp(self):
        Author.objects.create(author_name='harsha')

    def test_author_name(self):
        author= Author.objects.get(author_name='harsha')
        self.assertEqual(author.get_author(),'harsha')

# class Author(models.Model):
#     author_name = models.CharField(max_length=100, help_test='enter author name')
#
#     def __str__(self):
#        return self.author_name

