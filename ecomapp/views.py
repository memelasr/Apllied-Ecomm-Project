from django.shortcuts import render
from .models import Products
from .models import Customers


# Create your views here.

def home(request):
    context={
        'home': home.objects.all()
    }
    return render(request, 'home.html', context)


def products(request):
    context={
          'products' : Products.objects.all()
    }
    return render(request, 'products.html', context)
 
def new_customer(request):
    context={
          'customers' : Customers.objects.all()
    }
    return render(request, 'new_customer.html', context)
 
def new_customer(request):
    if request.method == 'POST':
        Firstname = request.POST['fname']
        Lastname = request.POST['Lname']
        ID = request.POST['id']
        Title = request.POST['title']
        Gender = request.POST['1option']
        Nationality = request.POST['country']
        Address = request.POST['street_name']
        Suburb = request.POST['suburb']
        City = request.POST['city']
        Postcode = request.POST['postcode']
        Phone = request.POST['phone']
        Alt_phone = request.POST['alt_phone']
        Email = request.POST['email']

        new_customer = Customers(
            fname=Firstname,
            Lname=Lastname,
            id=ID,title=Title,gender=Gender,
            country=Nationality,street_name=Address,
            suburb=Suburb,city=City,postcode=Postcode,
            phone=Phone,alt_phone=Alt_phone,
            email=Email)
        new_customer.save()
        
        return render(request, 'new_customer.html',{} )