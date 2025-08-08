from django.contrib import admin
from django.urls import path
from clientes.views import ClienteListCreateView
from ordens.views import OrdemServicoListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', ClienteListCreateView.as_view()),
    path('ordens/', OrdemServicoListCreateView.as_view()),
]
