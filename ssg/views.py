from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Destination, Demo

 #Create your views here.

def cpage(request):
        
    if request.method == 'POST':
        contact=Destination()
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        contact.name=name
        contact.email=email
        contact.massage=massage

        contact.save();
        print('contact created')
        return redirect('/')
    else:
        return render(request, "cpage.html")


def hp(request):

    dem = Demo.objects.all()

    return render(request, "hp.html", {'dem': dem})

#def cpage(request):
#    return render(request, "cpage.html")
