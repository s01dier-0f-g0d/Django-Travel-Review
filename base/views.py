from django.shortcuts import render

# Create your views here.

from .models import Destination, Country
from django.shortcuts import render,redirect,get_object_or_404
from base.forms import DestinationForm,CountryForm
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone


# --------------------------------------------------------------------------------#
                                # Country #
# --------------------------------------------------------------------------------#

def create_country(request):
    form= CountryForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request,'Country Created Successfully')
        return redirect('read_country')
    return render(request, 'create_country.html', {'form': form})

#Read Country
def read_country(request):
    search=request.GET.get('q')
    if search:
        data=Country.objects.filter(
            Q(name__icontains=search)|
            Q(description__icontains=search)|
            Q(code__icontains=search)|
            Q(status__icontains=search)
        )
    else:
        data=Country.objects.all()
    return render(request, 'read_country.html',{'data':data, 'search':search})

#Update Country
def update_country(request, pk):
    data = get_object_or_404(Country, id=pk)
    if request.method=='POST':  
        form = CountryForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Country Updated Successfully')
            return redirect('read_country')
    else:
        form=CountryForm(instance=data)
    return render(request,'update_country.html',{'form': form})

#Delete Country
def delete_country(request, pk):
    data = get_object_or_404(Country, id=pk)
    if request.method == 'POST':
        data.delete()
        messages.success(request,'Country Deleted Successfully')
        return redirect('read_country')
    return render(request, 'delete_country.html', {'data': data})


# --------------------------------------------------------------------------------#
                                # Destination #
# --------------------------------------------------------------------------------#

def home(request):
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
        data=Destination.objects.filter(is_deleted=False)

    return render(request,'display.html',{'data':data})

def update(request,key):
    data = get_object_or_404(Destination, id=key)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request,'Review has been Modified')
            return redirect('display')
    else:
        form = DestinationForm(instance=data)
    return render(request,'update.html',{'form':form})

def deleteDestination(request,key):
    data=get_object_or_404(Destination, id=key)
    if request.method =='POST':
        data.is_deleted=True #data.delete() deletes data permanently
        data.deleted_at=timezone.now()
        data.save()
        messages.success(request,'Review Deleted')
        return redirect('display')
    return render(request,'deleteDest.html',{'data':data})

def specific(request,key):
    data = get_object_or_404(Destination, id=key)
    return render(request,'specific.html',{'data':data})

def create(request):
    form=DestinationForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request,'Review created successfully')
        return redirect('display')
    return render(request,'create.html',{'form':form})

#History
def Destination_history(request):
    search=request.GET.get('q')
    if search:
        data= Destination.objects.filter(
            Q(title__icontains=search)|
            Q(desc__icontains=search)|
            Q(genre__icontains=search) 
        )
    else:
        data=Destination.objects.filter(is_deleted=True)
    return render(request,'history.html',{'data':data})

#Restore
def restore_Destination(request, pk):
    data=get_object_or_404(Destination, id=pk, is_deleted=True)
    if request.method=='POST':
        data.is_deleted=False
        data.deleted_at=None
        data.save()
        messages.success(request, "Destination Restored Successfully")
        return redirect('history')
    return render(request, 'restore.html', {'data':data})