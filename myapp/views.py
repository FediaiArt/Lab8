from django.shortcuts import render
from .models import Film, Cinema, FilmScreening

def project_info(request):
    tables_data = {
        'Фільми': Film.objects.values(),
        'Кінотеатри': Cinema.objects.values(),
        'ТранслюванняФільмів': FilmScreening.objects.values()
    }

    return render(request, 'project_info.html', {'tables_data': tables_data})
