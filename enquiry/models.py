from django.db import models
from courses.models import Courses
from branches.models import Branches

# Create your models here.

class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    courseId = models.ForeignKey(Courses, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=50)
    contact = models.PositiveBigIntegerField()
    address = models.TextField(max_length=1024)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)