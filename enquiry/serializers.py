from rest_framework import serializers
from .models import Enquiry
from courses.serializers import CoursesSerializer
from branches.serializers import BranchesSerializer

class EnquirySerializer(serializers.ModelSerializer):

    courseId_id = serializers.IntegerField(write_only=True)
    courseId = CoursesSerializer(read_only=True)

    branch_id = serializers.IntegerField(write_only=True)
    branch = BranchesSerializer(read_only=True)

    #specify model name & field inside meta class
    class Meta:
        model = Enquiry
        fields = ['id','name','education','courseId_id','courseId','email','gender','contact','address','branch_id','branch']
        read_only_fields = ['id']

    #add custom validator 
    def validate(self, data):
        if(len(data['name'])) == 0:
            raise serializers.ValidationError({'error':'name required'})
        return data