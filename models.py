from django.db import models
from django.utils import timezone

# Create your models here.


class Title(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = timezone.now()


def publish(self):
    self.published_date = timezone.now()
    self.save()

    return self.published_date

def __str__(self):
    return self.title
