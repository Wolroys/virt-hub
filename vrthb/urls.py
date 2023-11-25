from django.urls import path
from .views import index, profile_view, register_view, create_view

urlpatterns = [
    path('', index, name='index_url'),
    path('profile/', profile_view, name='profile_url'),
    path('register/', register_view, name='register_url'),
    path('create/', create_view, name='create_url')
]
