from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))

def read_csv():
    csvFilename = 'data-398-2018-08-30.csv'
    with open(csvFilename, encoding='utf-8') as csvfile:
        rows = csv.reader(csvfile, delimiter=",")
        tmp = list(rows)
    bus_station = {}
    for i in tmp:
        print("name:{} street:{} district:{}".format(i[1], i[4], i[6]))
        bus_station[i[8]] = {'name': i[1], 'street': i[4], 'district': i[6]}
    return bus_station

def pagi(request):
    paginator = Paginator([str(i) for i in range(100)], 15)
    page = paginator.get_page(5)
    context = {'page': page}
    return render(request, 'stations/index.html', context)

def get_bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    csvFilename = 'data-398-2018-08-30.csv'
    with open(csvFilename, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        bus_stations = list(reader)
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(bus_stations, 5)
        page = paginator.get_page(page_number)
        context = {
             'bus_stations': bus_stations,
             'page': page,
        }
    return render(request, 'stations/index.html', context)
