from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.index, name= 'index'),
    path('navbar/', views.navbar, name='navbar'),
    path('addfilm/', views.add_film, name='add_film'),
    path('adddirector', views.add_director, name='add_director')
]

