from django.shortcuts import render
from rest_framework import generics
from .models import Email, Product
from .serializers import EmailSerializers, ProductSerializers


class EmailAPIVIew(generics.CreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializers



class ProductAPIVIew(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


#  orozbek gulmuradov