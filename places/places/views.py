from .models import Place
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json


def check_variable(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept": "application/json"})
    variables = r.json()
    for variable in variables:
        if data["variable"] == variable["id"]:
            return True
    return False


def PlaceList(request):
    queryset = Place.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)


def PlaceCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_variable(data_json) == True:
            place = Place()
            place.variable = data_json['id']
            place.value = data_json['name']
            place.save()
            return HttpResponse("successfully created place")
        else:
            return HttpResponse("unsuccessfully created place. Variable does not exist")


def PlacesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        places_list = []
        for place in data_json:
            if check_variable(place) == True:
                db_place = Place()
                db_place.variable = place['id']
                db_place.value = place['name']
            else:
                return HttpResponse("unsuccessfully created places. Variable does not exist")

        Place.objects.bulk_create(places_list)
        return HttpResponse("successfully created places")
