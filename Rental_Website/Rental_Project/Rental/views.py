from django.shortcuts import render
from .models import Rental
from .forms import ContactForm

def all_rental(request):
    rental= Rental.objects.all()
    return render(request, 'all_rental.html',{'all_rental':rental})

def single_rental(request, pk):
    one_rental= Rental.objects.get(id= pk)
    return render(request, 'single_rental.html', {'one_rental': one_rental})

def add_rental(request):
    customers = Customer.objects.all()
	rented_list = Rental.objects.filter(return_date__isnull=True).values('vehicle_id')
	unrented_list = Vehicle.objects.exclude(pk__in=rented_list)
	
	if request.method == 'POST':
		cust_id = request.POST.get('customer_id')
		vehicle_id = request.POST.get('vehicle_id')
		vehicle = Vehicle.objects.filter(id=vehicle_id).first()
		customer = Customer.objects.filter(id=cust_id).first()
		vehicle_rentals = Rental.objects.filter(vehicle_id=vehicle_id, return_date__isnull=True).first()

		if customer is None: 
			#flash message with no cust found
			return render(request, 'add_rental.html',{'customers' : customers})

		elif vehicle is None:
			#flash message with no vehicle found
			return render(request, 'add_rental.html',{'customers' : customers})

		elif vehicle_rentals is not None:
			#flash message that vehicle is rented out
			return render(request, 'add_rental.html',{'customers' : customers})

		rental = Rental(rental_date=timezone.now(),customer=customer,vehicle=vehicle)
		rental.save()
		return redirect('all_rentals')
	return render(request, 'add_rental.html',{'customers' : customers, 'unrented_list' : unrented_list})


