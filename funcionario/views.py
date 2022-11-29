from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from funcionario.models import Funcionario



class FuncionariosView(ListView):
    model = Funcionario
    template_name = 'funcionario.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionariosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs
