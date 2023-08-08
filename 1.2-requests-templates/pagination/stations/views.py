from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV
import csv



def index(request):
    return redirect(reverse('bus_stations'))

def read_csv():
    with open(BUS_STATION_CSV, encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile, delimiter=",")
        tmp = list(rows)
    bus_station = []
    for i in tmp:
        tmp = {'Name': i[1],
               'Street': i[4],
               'District': i[6]
               }
        bus_station.append(tmp)
    return bus_station

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    paginator = Paginator(list(read_csv()), 5)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)

    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
