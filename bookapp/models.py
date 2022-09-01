from django.db import models
from django.contrib.auth.models import User

class BookShelf(models.Model):
    """Creating a book shelf data"""
    name=models.CharField(max_length=100,blank=True)
    author=models.CharField(max_length=100,blank=True)
    ISBN_number=models.IntegerField()
    publication=models.DateTimeField(auto_now_add=True,blank=True)
    genre=models.CharField(max_length=100,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
