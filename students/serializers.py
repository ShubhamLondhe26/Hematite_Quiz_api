from rest_framework import serializers
from .models import Student
from branches.serializers import BranchesSerializer

class StudentSerializer(serializers.ModelSerializer):

    branch_id = serializers.IntegerField(write_only=True)
    branch = BranchesSerializer(read_only=True)

    #specify model name & field inside meta class
    class Meta:
        model = Student
        fields = ['id','name','email','contact','gender','branch','prnNo','otherBranch','branch','branch_id']
        read_only_fields = ['id']

    #add custom validator 
    def validate(self, data):
        if(len(data['name'])) == 0:
            raise serializers.ValidationError({'error':'name required'})
        return data