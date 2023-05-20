from django.urls import include, path
from . import views

urlpatterns = [
    path('email/api/', views.EmailAPIVIew.as_view(), name='email')
]