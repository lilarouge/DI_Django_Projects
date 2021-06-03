from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage/', views.ContactForm.as_view(), name='homepage'),
    path('booking/', views.newbooking, name='newbooking'),
    path('rooms/', views.DisplayRooms, name='all_rooms'),
    path('addroom/', views.AddRoom.as_view(), name='add_room'),

]