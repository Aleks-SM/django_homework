from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV
import csv



def index(request):
    return redirect(reverse('bus_stations'))

def read_csv():
    csvFilename = BUS_STATION_CSV
    with open(csvFilename, encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile, delimiter=",")
        tmp = list(rows)
    bus_station = {}
    for i in tmp:
        bus_station[i[8]] = {'name': i[1],
                             'street': i[4],
                             'district': i[6]
                             }
    return bus_station

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(BUS_STATION_CSV, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')

        stations = list(reader)
    paginator = Paginator(stations, 5)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)

    context = {
         'bus_stations': page,
         'page': page,
    }
    return render(request, 'stations/index.html', context)
