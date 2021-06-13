from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage/', views.ContactForm.as_view(), name='homepage'),
    path('booking/', views.book_dates, name='book_dates'),
    path('booking/<str:check_in>/<str:check_out>/', views.book_room, name='book_room'),
    path('rooms/', views.DisplayRooms, name='all_rooms'),
    # path('addroom/', views.AddRoom.as_view(), name='add_room'),
    path('addroom/', views.AddRoom, name='add_room'),

]