from rest_framework import serializers
from .models import Courses

class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = '__all__'
        read_only_fields = ['id']

    #add custom validator
    def validate(self,data):
        if(len(data['courseName'])) == 0:
            raise serializers.ValidationError({'error':"courseName should not be empty"})
        return data