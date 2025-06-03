from pyexpat import model
from shutil import ExecError
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse

from customers.models import Car, Customer

def customers(request):
    if request.method == "GET":
        return render(request, 'customers.html')
    elif request.method == "POST":
        save_customer(request)

def save_customer(request):
    name = request.POST.get('name')
    surname = request.POST.get('surname')
    document = request.POST.get('document')
    email = request.POST.get('email')

    car_models = request.POST.getlist('car-model')
    car_plates = request.POST.getlist('car-plate')
    car_years = request.POST.getlist('car-year')

    customer = Customer(
            name=name, 
            surname=surname,
            email=email, 
            document=document
        )
    customer.validate_constraints() #todo overwrite the form with ModelForm from django
    try:
        customer.save()
    except IntegrityError as e:
        print(e.__str__())
        render

    for index in range(len(car_models)):
        Car(
                model= car_models[index],
                plate= car_plates[index],
                year= car_years[index],
                customer=customer
            ).save()
