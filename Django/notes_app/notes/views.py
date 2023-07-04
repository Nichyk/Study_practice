from django.shortcuts import render
from .models import Notes


def index(request):
    notes = Notes.objects.all()
    return render(request, 'index.html', {'notes': notes})
