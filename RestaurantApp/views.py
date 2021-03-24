from django.shortcuts import render,redirect
from .forms import ReserveForm
from . import models

def index(request):
    SpecialFood=models.Food.objects.filter(SpecialFood=True)
    Food=models.Food.objects.all()
    Fcategories=models.FoodCategory.objects.all()
    return render(request,'index.html',{'SpecialFood':SpecialFood,'foods':Food,'Fcategories':Fcategories})

def reservation(request):
    form =ReserveForm()
    if request.method=="POST":
        form=ReserveForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/index")
    return render(request,'reservation.html',{'form':form})

def contact(request):
    return render(request,'contact.html' )

def about(request):
    return render(request,'about.html' )

def fooddetailsview(request,id):
    food=models.Food.objects.get(id=id)
    return render(request,'fooddetails.html',{'food':food})


