from django.shortcuts import render

from .models import Aula

# Create your views here.
def list_aulas(request):
    context = {
        'aulas': Aula.objects.all()
    }

    return render(request, 'list_aulas.html', context)
