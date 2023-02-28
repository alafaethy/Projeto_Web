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
    cota = Ticket.objects.all().aggregate(Sum('cota'))['cota__sum']

    som = cota * total
    
    a = f'{som:.2f}'
    if request.method == "GET":
        return JsonResponse({'total' : a}) # SOMAR TODO FATURAMENTO DO BD.Vendas


def return_lucro(request):
    rendimento = Ticket.objects.all().aggregate(Sum('ultimo_rendimento'))['ultimo_rendimento__sum']
    cota = Ticket.objects.all().aggregate(Sum('cota'))['cota__sum']
    
    dev = rendimento * cota

    a = f'{dev:.2f}'
    if request.method == "GET":
        return JsonResponse({'rendimento': a})

def delete(request,id):
    tickets = Ticket.objects.get(id=id)
    print(tickets)
    tickets.delete()
    return redirect("teste")



def add(request):
    if request.method == "POST":
        ticket = request.POST.get("ticket")
        company = request.POST.get("company")
        
        emp = Ticket(
            ticket = ticket,
            company = company,
            
        )
        try:
            emp.save()
            return redirect("teste")
        except ValueError as err:
            print("NAO SALVO", err)
        
    return redirect("teste")


def edit(request,id):
    cota = Ticket.objects.all()
    
    ctx = {
        'cota':cota
    }
    
    
    
    return redirect(request,"teste",ctx)