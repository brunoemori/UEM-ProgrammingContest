from django.db import models
from signup.models import CustomUser

class Article(models.Model):
    title = models.CharField(max_length=64, default='')
    date = models.DateTimeField(default='')
    authorID = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default='')
    problemNumber = models.PositiveIntegerField()
    language = models.CharField(max_length=1)
    inputs = models.TextField(default='')
    outputs = models.TextField(default='')
    body = models.TextField(default='')
    bodyCode = models.TextField(default='')
    solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('authorID', 'problemNumber', 'language')

