from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('company/<str:slug>/', CompanyDetailView.as_view(), name='company'),
    path('recipe-detail/<int:pk>/', FoodDetailView.as_view(), name='detail'),
]
