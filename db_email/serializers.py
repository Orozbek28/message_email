from rest_framework import serializers
from .models import Email


class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

 


