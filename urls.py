from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('', views.index),
    path('userList/', views.user_list),
    path('userDetail/<int:pk>/', views.user_detail),
]
