from django.urls import path
from . import views
from .views import post_edit, post_list

urlpatterns = [
    path('', views.login, name='login'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/editar/', post_edit, name='post_edit'),
]