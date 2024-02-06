from django.db import models

# Create your models here.

class Voucher(models.Model):
    voucherCode = models.CharField(max_length = 125)
