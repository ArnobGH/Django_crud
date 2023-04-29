from django.shortcuts import render, redirect
from .models import *
from django import forms
from .filters import *

# Create your views here.
def home(request):
    bms=Books.objects.all()


    return render(request,"bms/home.html",{'bms':bms})

def add(request):
    if request.method=='POST':
        bo_idn=request.POST.get("b_idn")
        bo_name=request.POST.get("b_name")
        bo_rName=request.POST.get("b_rName")
        bo_rAge=request.POST.get("b_rAge")
        bo_page=request.POST.get("b_page")
        bo_date=request.POST.get("b_date")
        bo_type=request.POST.get("b_type")
        b=Books()
        b.idn=bo_idn
        b.name=bo_name
        b.rName=bo_rName
        b.rAge=bo_rAge
        b.page=bo_page 
        b.date=bo_date
        b.type=bo_type

        b.save()
        return redirect("/bms/home")
    return render(request,"bms/add.html",{})

def delete(request,idn):
    b=Books.objects.get(pk=idn)
    b.delete()
    return redirect('/bms/home/')

def update(request,idn):
    bms=Books.objects.get(pk=idn)
    return render(request,"bms/update.html",{'bms':bms})

def do_update(request,idn):
    bo_idn=request.POST.get("b_idn")
    bo_name=request.POST.get("b_name")
    bo_rName=request.POST.get("b_rName")
    bo_rAge=request.POST.get("b_rAge")
    bo_page=request.POST.get("b_page")
    bo_date=request.POST.get("b_date")
    bo_type=request.POST.get("b_type")
    b=Books()
    b.idn=bo_idn
    b.name=bo_name
    b.rName=bo_rName
    b.rAge=bo_rAge
    b.page=bo_page 
    b.date=bo_date
    b.type=bo_type

    b.save()
    return redirect("/bms/home")

def search(request):
    return render(request,"bms/home.html",{})