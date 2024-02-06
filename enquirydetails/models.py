from django.db import models

# Create your models here.

class EnquiryModel(models.Model):
    name = models.CharField(max_length = 125, blank = False)
    education = models.CharField(max_length = 125)
    collegeAndCity = models.CharField(max_length = 125)
    yearOfPassing = models.IntegerField()
    inPuneSince = models.IntegerField()
    experience = models.CharField(max_length = 125)
    contact = models.PositiveBigIntegerField()
    email = models.EmailField(max_length = 125)
    courseInterested = models.CharField(max_length=200)
    reference = models.CharField(max_length = 125)
    batchType = models.CharField(max_length = 125)
    comment = models.TextField()
    