from django.shortcuts import render

# Create your views here.

from .models import Destination
from django.shortcuts import render,redirect,get_object_or_404
from base.forms import DestinationForm
from django.contrib import messages
from django.db.models import Q

def home(request):
    # form=DestinationForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     messages.success(request,'Destination Created. Viel Gluck !')
    #     return redirect('display')
    return render(request, 'home.html')


def display(request):
    search = request.GET.get('q')
    if search:
        data=Destination.objects.filter(
            Q(name__icontains=search) |
            Q(rating__icontains=search) |
            Q(average_cost__icontains=search) |
            Q(country__icontains=search) 
        )
    else:
        data = Destination.objects.all()
    return render(request,'display.html',{'data':data})

def update(request,key):
    data = get_object_or_404(Destination, id=key)
    form = DestinationForm(request.POST or None, instance=data)
    if form.is_valid():
        form.save()
        messages.success(request,'Review has been Modified')
        return redirect('display')
    return render(request,'update.html',{'form':form})

def deleteDestination(request,key):
    data=get_object_or_404(Destination, id=key)
    if request.method =='POST':
        data.delete()
        messages.success(request,'Review Deleted')
        return redirect('display')
    return render(request,'deleteDest.html',{'data':data})

def specific(request,key):
    data = get_object_or_404(Destination, id=key)
    return render(request,'specific.html',{'data':data})

def create(request):
    form=DestinationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Review created successfully')
        return redirect('display')
    return render(request,'create.html',{'form':form})