from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard,name="dashboard"),
    path("teste/",views.teste, name="teste"),
    path("return_total/", views.return_total,name="return_total"),
    path("return_profit/", views.return_lucro,name="return_lucro"),
    path("delete/<int:id>",views.delete, name='delete'),
    path("add/",views.add,name="add"),
    path("edit/<int:id>",views.edit, name='edit')
]