from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('users/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('testing2', views.testing2, name='testing2'),
    path('firstname', views.firstname, name='firstname'),
    path('lastname', views.lastname, name='lastname'),
    path('filter', views.filter, name='filter'),
    path('css', views.css, name='css'),
]
