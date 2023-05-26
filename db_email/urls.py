from django.urls import include, path
from . import views

urlpatterns = [
    path('email/api/', views.EmailAPIVIew.as_view(), name='email'),
    path('product/api/', views.ProductAPIVIew.as_view(), name='product')
]