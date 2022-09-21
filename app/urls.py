from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_task/', create_task, name='create_task'),
    path('update_task/<int:pk>/', update_task, name='update_task'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),
]