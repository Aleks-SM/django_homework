import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = '{} часов {} минут'.format(datetime.now().hour + 4, datetime.now().minute)
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    try:
        template_name = 'app/workdir.html'
        path = "first_project"
        list_of_files = os.listdir(os.path.join(os.getcwd(), path))
        context = {'list_of_files': list_of_files}
        return render(request, template_name, context)
    except Exception:
        raise NotImplemented
