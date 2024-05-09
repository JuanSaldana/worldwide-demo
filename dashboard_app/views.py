from django.shortcuts import render
from .models import Artist


def index(request):
    Artist(artistic_name="Juan").save()
    return render(request, 'dashboard/index.html', {})
