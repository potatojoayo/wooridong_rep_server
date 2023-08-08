from rest_framework import serializers
from ..models import RepVerificationMessage 

class RepVerificationMessageSerializer(serializers.ModelSerializer):

    class Meta:

        model = RepVerificationMessage 
        fields = '__all__' 
        extra_kwargs = {'rep':{'read_only': True,},}
