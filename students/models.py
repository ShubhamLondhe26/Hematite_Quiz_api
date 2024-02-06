from django.db import models
from django.core.validators import MaxValueValidator
from branches.models import Branches

# Create your models here.
class Student(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact = models.PositiveBigIntegerField()
    gender = models.CharField(max_length=50)
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    prnNo = models.IntegerField(validators=[MaxValueValidator(9999999999999999)])
    otherBranch = models.CharField(max_length=100)
