from django.shortcuts import render, redirect
from django.urls import reverse
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
        # print("name:{} street:{} district:{}".format(i[1], i[4], i[6]))
        bus_station[i[8]] = {'name': i[1], 'street': i[4], 'district': i[6]}

    return bus_station

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    # print(read_csv())
    # < td > {{station.Name}} < / td >
    # < td > {{station.Street}} < / td >
    # < td > {{station.District}} < / td >
    # context = {
    # #     'bus_stations': ...,
    # #     'page': ...,
    # }
    context = read_csv()
    # print(context.get('ДК Зуева'))
    print(context.keys())
    return render(request, 'stations/index.html', context)
