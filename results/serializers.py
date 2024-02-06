from rest_framework import serializers
from .models import Results
from exams.serializers import ExamSerializer
from  students.serializers import StudentSerializer

class ResultSerializer(serializers.ModelSerializer):
    studentId_id = serializers.IntegerField(write_only=True)
    studentId = StudentSerializer(read_only=True)
    examId_id = serializers.IntegerField(write_only=True)
    examId = ExamSerializer(read_only=True)
    
    class Meta:
        model = Results
        fields = ['id','studentId_id','examId_id','examId','studentId','totalMarks','obtainedMarks','status','grade','examDate']
        read_only_fields = ['id']
        