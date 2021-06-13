from visitors.models import *
from visitors.forms import *
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'homepage.html')

def book_dates(request):
    form= BookingDatesForm()

    if request.method == "POST":
        check_in= request.POST["check_in"]
        check_out= request.POST["check_out"]
        return redirect("book_room", check_in, check_out)

    return render(request, 'book_dates.html', {"form":form})

def book_room(request, check_in, check_out):
    form = BookingRoomForm()
    form.fields['room'].queryset = Rooms.objects.filter(
        Q(bookings__check_in__gt=check_out)|
        Q(bookings__check_out__lt=check_in)|
        Q(bookings=None)
    )
    if request.method == "POST":
        return redirect("homepage")
    return render(request, "book_room.html", {"form": form})


def DisplayRooms(request):
    rooms= Rooms.objects.all()

    return render(request, 'all_rooms.html', {'rooms': rooms})


# class AddRoom(generic.CreateView):
#     template_name='forms.html'
#     model= Rooms
#     fields= '__all__'
#     success_url=reverse_lazy('homepage')

    # @login_required
    # def form_valid(self, form):
    #     post_to_add= form.cleaned_data
    #     # print(post_to_add)
    #     return super().form_valid(form)
@login_required
def AddRoom(request):
    if not request.user.is_superuser:
        return redirect('login')
    form = Rooms_update()
    if request.method == 'POST':
        form = Rooms_update(request.POST, request.FILES)
        print(request.POST)
        print(form)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_rooms')
        else:
            print(form.errors)
    return render(request, 'forms.html', {'form':form})

class ContactForm(generic.CreateView):
    template_name='homepage.html'
    model= ContactForm
    fields= '__all__'
    success_url=reverse_lazy('homepage')

    def form_valid(self, form):
        post_to_add= form.cleaned_data
        # print(post_to_add)
        return super().form_valid(form)




