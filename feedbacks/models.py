from django.db import models
from phone_field import PhoneField
from branches.models import Branches

# Create your models here.
class Feedback(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    contact = PhoneField(help_text='Contact phone number')
    branch = models.ForeignKey(Branches, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=120)