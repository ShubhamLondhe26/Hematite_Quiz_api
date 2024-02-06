from rest_framework import serializers
from .models import Batches
from courses.serializers import CoursesSerializer

class BatchesSerializer(serializers.ModelSerializer):

    courseId_id = serializers.IntegerField(write_only=True)
    courseId = CoursesSerializer(read_only=True)

    class Meta:
        model = Batches
        fields = ['courseId_id', 'courseId', 'batchType', 'startDate', 'startDate', 'seatAvailable', 'duration', 'batchStatus']
        read_only_fields = ['id']

    #add custom validator
    def validate(self, data):
        if(len(data['batchType'])) == 0:
            raise serializers.ValidationError({'error':"batchType should not be empty"})
        return data