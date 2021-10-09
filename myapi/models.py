# models.py

from django.db import models
class Homework(models.Model):
    subject = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.subject