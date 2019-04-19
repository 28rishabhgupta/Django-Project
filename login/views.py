from django.http import HttpResponse
from django.shortcuts import render
from .models import Login


def index(request):
    login = Login.objects.all()
    return render(request, 'index.html', {'login': login})

