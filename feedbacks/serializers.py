from rest_framework import serializers
from .models import Feedback
from branches.serializers import BranchesSerializer

class FeedbacksSerializer(serializers.ModelSerializer):

    branch_id = serializers.IntegerField(write_only=True)
    branch = BranchesSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['name','email','contact','branch_id','branch','answer1']
        read_only_fields = ['id']

    #add custom validator
    def validate(self,data):
        if(len(data['name'])) == 0:
            raise serializers.ValidationError({'error':"name should not be empty"})
        return data