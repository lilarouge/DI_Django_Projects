from django.urls import path
from . import views

urlpatterns = [
    path('rental/', views.all_rental, name='all_rental'),
    path('rental/<int:pk>', views.single_rental, name='single_rental'),
    path('rental/add/', views.add_rental, name='add_rental'),
]