from django.db import models
from category.models import Category
from author.models import Author


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    decription = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f'{self.title} By {self.author.author.username}'