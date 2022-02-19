from django.db import models

# Create your models here.


class Submission(models.Model):
    author = models.CharField(max_length=120)
    count = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author


class Comment(models.Model):
    author = models.CharField(max_length=120)
    count = models.IntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author
