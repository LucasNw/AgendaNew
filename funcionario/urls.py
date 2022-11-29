from django.urls import path
from .views import FuncionariosView


urlpatterns = [
    path('clientes', FuncionariosView.as_view(), name= 'funcionario')
]