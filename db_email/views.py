from django.shortcuts import render
from rest_framework import generics
from .models import Email
from .serializers import EmailSerializers


class EmailAPIVIew(generics.CreateAPIView):
    serializer_class = EmailSerializers
    queryset = Email.objects.all()

#  orozbek gulmuradov