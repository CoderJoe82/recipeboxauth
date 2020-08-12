from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=80)
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.author.name}"