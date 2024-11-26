from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def wheter(request):
    return render(request,'wheter_p.html')

def portfolio(request):
    return render(request,'portfolio.html' )

def contact(request):
    if request.method == 'POST':

        
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"Name: {name}, Email: {email}, Message: {message}")  # Debugging print

       
        try:
            contact_instance = Contact(name=name, email=email, message=message)
            contact_instance.save()
            return HttpResponse("<h3>Thank you for connecting, Sandeep!</h3>")
        except Exception as e:
            return HttpResponse("<h2>Contact failed</h2>")
        
    return render(request, 'home.html')
         


    
        
        

        
        