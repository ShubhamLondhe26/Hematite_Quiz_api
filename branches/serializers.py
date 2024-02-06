from rest_framework import serializers
from .models import Branches

class BranchesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branches
        fields = '__all__'
        read_only_fields = ['id']

    #add custom validator
    def validate(self,data):
        if(len(data['branchName'])) == 0:
            raise serializers.ValidationError({'error':"branchName should not be empty"})
        return data