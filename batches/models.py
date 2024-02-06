from django.db import models
from courses.models import Courses

# Create your models here.
class Batches(models.Model):

    courseId = models.ForeignKey(Courses,  on_delete=models.CASCADE)
    batchType = models.CharField(max_length=100)
    startDate = models.DateField()
    batchTime = models.CharField(max_length=50)
    seatAvailable = models.BooleanField(default=True)
    duration = models.CharField(max_length=50)
    batchStatus = models.CharField(max_length=50)