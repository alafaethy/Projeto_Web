from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard,name="dashboard"),
    path("teste/",views.teste, name="teste"),
    path("return_total/", views.return_total,name="return_total"),
    path("return_lucro/", views.return_lucro,name="return_lucro"),
]