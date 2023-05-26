from django.shortcuts import render
from rest_framework import generics
from .models import Email, Product
from .serializers import EmailSerializers, ProductSerializers


class EmailAPIVIew(generics.CreateAPIView):
    serializer_class = EmailSerializers
    queryset = Email.objects.all()


class ProductAPIVIew(generics.ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

#  orozbek gulmuradov