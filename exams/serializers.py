from rest_framework import serializers
from .models import Exam

class ExamSerializer(serializers.ModelSerializer):
    
    #specify model name & field inside meta class
    class Meta:
        model = Exam
        fields = "__all__"
        read_only_fields = ['id']

    #add custom validator 
    def validate(self, data):
        if(len(data['examName'])) == 0:
            raise serializers.ValidationError({'error':'exam-name required'})
        return data