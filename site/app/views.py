from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Ticket
from datetime import datetime
from django.db.models import Sum

# Create your views here.
def home(request):
    return render(request, "index.html")

def dashboard(request):
    return render(request,"dashboard.html")

def teste (request):
    return render(request,"teste.html")


def  return_total(request):
    total = Ticket.objects.all().aggregate(Sum('price'))['price__sum']
    cota = Ticket.objects.all().aggregate(Sum('cota'))['cota__sum']

    som = cota * total
    
    
    if request.method == "GET":
        return JsonResponse({'total' : som}) # SOMAR TODO FATURAMENTO DO BD.Vendas


def return_lucro(request):
    rendimento = Ticket.objects.all().aggregate(Sum('ultimo_rendimento'))['ultimo_rendimento__sum']
    cota = Ticket.objects.all().aggregate(Sum('cota'))['cota__sum']
    
    dev = rendimento * cota


    if request.method == "GET":
        return JsonResponse({'rendimento': dev})