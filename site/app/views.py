from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import Ticket
from datetime import datetime
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request,"dashboard.html")

def teste (request):
    tabelas = Ticket.objects.all()
    return render(request,"teste.html", {"tabelas":tabelas})
    
    # return render(request,"teste.html")


def  return_total(request):
    total = Ticket.objects.all().aggregate(Sum('price'))['price__sum']



    if request.method == "GET":
        return JsonResponse({'total' : total}) # SOMAR TODO FATURAMENTO DO BD.Vendas


def return_lucro(request):
    rendimento = Ticket.objects.all().aggregate(Sum('rendimento'))['rendimento__sum']
    
    dev = rendimento * 1

    a = f'{dev:.2f}'
    if request.method == "GET":
        return JsonResponse({'rendimento': a})

def delete(request,id):
    tickets = Ticket.objects.get(id=id)
    tickets.delete()
    return redirect("teste")



def add(request):
    if request.method == "POST":
        ticket = request.POST.get("ticket")
        company = request.POST.get("company")
        cota = request.POST.get("cota")
        price = request.POST.get("price")
        
        emp = Ticket(
            ticket = ticket,
            company = company,
            cota = cota,
            price = price,
            
        )
        try:
            emp.save()
            return redirect("teste")
        except ValueError as err:
            print("NAO SALVO", err)
        
    return redirect("teste")


def edit(request,id):
    # emp = Ticket.objects.all()
    
    # ctx = {
    #     'emp':emp
    # }
    # return redirect(request,"teste.html", ctx)
    cotas = Ticket.objects.get(id=id)
    return render(request,"edit.html", {"cota": cotas})


def update(request,id):
    if request.method == "POST":
        ticket = request.POST.get("ticket")
        company = request.POST.get("company")
        cota = request.POST.get("cota")
        price = request.POST.get("price")
        emp = Ticket(
            id = id,
            ticket = ticket,
            company = company,
            cota = cota,
            price = price,
            
            
        )
        emp.save()
        return redirect('teste')
    return redirect(request,"teste")