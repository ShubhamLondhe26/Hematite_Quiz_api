from rest_framework  import serializers
from .models import Voucher

class VoucherSeriaizer(serializers.ModelSerializer):
    
    class Meta:
        model = Voucher
        fields ='__all__'
        read_only_fields = ['id']
        
    #add custom validator
    def validate(self,data):
        if(len(data['voucherCode'])) == 0:
            raise serializers.ValidationError({'error':"Voucher code should not be empty"})
        return data