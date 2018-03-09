from django.db import models
from signup.models import CustomUser

class Article(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    authorID = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    problemNumber = models.PositiveIntegerField(unique=True)
    inputs = models.TextField(default='')
    outputs = models.TextField(default='')
    problemNumber = models.PositiveIntegerField(unique=True)
    body = models.TextField()
    bodyCode = models.TextField()

    def __str__(self):
        return self.title
