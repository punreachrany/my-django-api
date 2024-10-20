from django.urls import path
from .views import get_user, create_user, user_detail, get_test

urlpatterns = [
    path('users/', get_user, name="get_user"),
    path('users/create/', create_user, name="create_user"),
    path('users/<int:pk>', user_detail, name="user_detail"),
    path('test/', get_test, name="get_test"),
]
