from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
# Create your views here.

def index(request):
        context = {
                "variable1": "first value of variable",
                "variable2": "Second value of variable"

        }
        #return HttpResponse("This is Home page")
        return render(request, "index.html", context)

def about(request):
        #return HttpResponse("This is About page")
        return render(request, "about.html")


def available(request):
        #return HttpResponse("This is Available page")
        return render(request, "available.html")


def address(request):
        #return HttpResponse("This is Address page")
        return render(request, "address.html")

def contact(request):
        #return HttpResponse("This is Contact page")
        if request.method == "POST":
                name = request.POST.get('name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                more = request.POST.get('more')
                contact = Contact(name=name, email=email, phone=phone, more=more)
                contact.save()
                messages.success(request, 'Profile updated.')
        return render(request, "contact.html")







