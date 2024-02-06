from django.db import models

# Create your models here.
class Courses(models.Model):

    courseName = models.CharField(max_length=100)