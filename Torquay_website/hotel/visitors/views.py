from visitors.models import *
from visitors.forms import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
# from rest_framework import serializers


# Create your views here.
def index(request):
    return render(request, 'homepage.html')

def newbooking(request):
    if request.method == 'GET':
            return render (request, 'new_booking.html', {'form': BookingsForm, 'add_type': 'form'})
    if request.method == 'POST':
        data = request.POST
        form = BookingsForm(data)
        if form.is_valid():
            form.save()
    return redirect('homepage')

# def roomAvailable(validated_data):
#     available = False

#     # ...
#     # validation check here...
#     # ...

#     return available


# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bookings
#         fields = '__all__'

#     def create(self, validated_data):
#         if roomAvailable(validated_data):
#             return Bookings.objects.create(**validated_data)
#         else:
#             raise serializers.ValidationError({
#                 "detail": "Room is not available for these dates."
#             })

#     def update(self, instance, validated_data):
#         if roomAvailable(validated_data):

#             instance.save()
#         else:
#             raise serializers.ValidationError({
#                 "detail": "Room is not available for these dates."
#             })
#         return instance



def DisplayRooms(request):
    rooms= Rooms.objects.all()

    return render(request, 'all_rooms.html', {'rooms': rooms})

class AddRoom(generic.CreateView):
    template_name='forms.html'
    model= Rooms
    fields= '__all__'
    success_url=reverse_lazy('homepage')

    def form_valid(self, form):
        post_to_add= form.cleaned_data
        # print(post_to_add)
        return super().form_valid(form)

class ContactForm(generic.CreateView):
    template_name='homepage.html'
    model= ContactForm
    fields= '__all__'
    success_url=reverse_lazy('homepage')

    def form_valid(self, form):
        post_to_add= form.cleaned_data
        # print(post_to_add)
        return super().form_valid(form)




