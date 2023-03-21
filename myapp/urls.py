from django.urls import path, include
from myapp.views import *
from rest_framework import routers

urlpatterns = [

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('usrsearch/',UserList.as_view()),
] 

