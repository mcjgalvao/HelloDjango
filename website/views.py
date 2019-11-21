from django.shortcuts import render
from HelloDjango.models import Funcionario

# Create your views here.
def index(request):
    
    funcionarios = Funcionario.objetos.all()
    
    contexto = {
        'funcionarios' : funcionarios
    }
    
    return render(
        request,
        "website/funcionarios.html",
        contexto
    )
    