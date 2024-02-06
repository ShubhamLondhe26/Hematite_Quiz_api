from django.db import models
from exams.models import Exam

# Create your models here.

class Question(models.Model):
    examId = models.ForeignKey(Exam, on_delete=models.CASCADE)
    questionText = models.TextField(max_length=1024)
    questionImage = models.FileField(upload_to='uploads/', null=True, blank=True)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)