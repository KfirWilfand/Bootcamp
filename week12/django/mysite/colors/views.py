from django.shortcuts import render
from django.http import HttpResponse
import json

colors = ['red', 'blue', 'black']


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_colors_list(request):
    return HttpResponse(json.dumps(colors), content_type="application/json")


def add_color(request):
    color = request.GET.get("color")
    if color in colors:
        return HttpResponse("The color is already exist!" ,status=409)

    colors.append(color)
    return HttpResponse(json.dumps(colors), content_type="application/json",status=291)


def get_color(request):
    color = request.GET.get("color")
    if color not in colors:
        return HttpResponse("no such color", status=404)

    return HttpResponse(json.dumps(color), content_type="application/json")
