from django.db import models

# Create your models here.

class Exam(models.Model):
    examName = models.CharField(max_length=100)
    examStatus = models.BooleanField(default=True)
