from django.shortcuts import render


def index(request):
    notes = ['Note 1', 'Note 2', 'Note 3']
    return render(request, 'index.html', {'notes': notes})
