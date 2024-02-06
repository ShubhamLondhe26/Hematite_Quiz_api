from rest_framework import serializers
from .models import Question
from exams.serializers import ExamSerializer

class QuestionSerializer(serializers.ModelSerializer):

    examId_id = serializers.IntegerField(write_only=True)
    examId = ExamSerializer(read_only=True)

    #specify model name & field inside meta class
    class Meta:
        model = Question
        fields = ['id','questionText','option1','option2','option3','option4','answer','examId','examId_id']
        read_only_fields = ['id']

    #add custom validator 
    def validate(self, data):
        if(len(data['questionText'])) == 0:
            raise serializers.ValidationError({'error':'questionText required'})
        return data

class QuestionDetailSerializer(serializers.ModelSerializer):
    #specify model name & field inside meta class
    class Meta:
        model = Question
        fields = QuestionSerializer.Meta.fields + ['questionImage']
        read_only_fields = ['id']

class QuestionImageSerializer(serializers.ModelSerializer):
    #specify model name & field inside meta class
    class Meta:
        model = Question
        fields = ['id','questionImage']
        read_only_fields = ['id']
        extra_kwargs = {'questionImage':{'required':True}}


