from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_gallery, name='gallery'),
    path('photo/<str:pk>/', views.view_photo, name='photo'),

    path('add_photo/', views.add_photo, name='add_photo'),

    path('update_photo/<str:pk>/', views.update_photo, name='update_photo'),

    path('delete_photo/<str:pk>/', views.delete_photo, name='delete_photo'),




]
