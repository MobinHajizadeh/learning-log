from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """something specific learned about topic"""

    # (foreign key for Topic, if topic deleted delete all entries)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # for true plural name of entry
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """return a string representation of the model"""
        return f"{self.text[:50]}..."
