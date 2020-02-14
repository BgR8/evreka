from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Navigation
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    thetime = datetime.now() - timedelta(hours=48)
    navs = Navigation.objects.filter(datetime__gte=thetime)

    return render(request, "index.html", {"navs": navs})

def addNav(request):
    if request.method == "GET":
        return redirect('/')
    else:
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        vehicle = request.POST.get('vehicle')
        ekle = Navigation(latitude = latitude, longitude = longitude, vehicle = vehicle)

        ekle.save()
        return redirect('/')

def update(request, id):
    nav = get_object_or_404(Navigation, id = id)
    
    nav.completed = not nav.completed

    nav.save()
    return redirect('/')

def delete(request, id):
    nav = get_object_or_404(Navigation, id = id)
    

    nav.delete()
    return redirect('/')