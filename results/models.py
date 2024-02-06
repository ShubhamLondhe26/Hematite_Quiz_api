from django.db import models
from students.models import Student
from exams.models import Exam

# Create your models here.

class Results(models.Model):
    studentId = models.ForeignKey(Student, on_delete=models.CASCADE)
    examId = models.ForeignKey(Exam, on_delete=models.CASCADE)
    totalMarks = models.IntegerField()
    obtainedMarks = models.IntegerField()
    status = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    examDate = models.DateField()