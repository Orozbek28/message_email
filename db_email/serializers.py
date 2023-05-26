from rest_framework import serializers
from .models import Email, Product


class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

 


