from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('photo/<str:pk>', views.view_photo, name = 'photo'),

    path('add_photo/', views.add_photo, name="add_photo"),
] 