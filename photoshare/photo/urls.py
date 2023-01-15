
from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery,name='gallery'),
    path('add/',views.add,name='add'),
    path('photo/<str:pk>/',views.photo,name='photos'),
]