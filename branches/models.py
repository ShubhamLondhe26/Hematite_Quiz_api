from django.db import models

# Create your models here.
class Branches(models.Model):
     
    branchName = models.CharField(max_length=100)
    branchStatus = models.BooleanField(default=True)
