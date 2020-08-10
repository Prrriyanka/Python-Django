from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Contact
from django.contrib import messages


def index(request):
    context={
        'variable' : 'FIrst Variable',
        'variable1': 'sEcond Variable'    }
    return render(request,"index.html",context)
#    return HttpResponse("homepage")

def about(request):
   return render(request, "about.html")

def services(request):
   return render(request, "services.html")

#Do not use spaces while entering name
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message was sent!!.')

    return render(request, "contact.html")


