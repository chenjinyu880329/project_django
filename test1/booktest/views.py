from django.shortcuts import render


from django.http import HttpResponse
from django.db.models import Max, F, Q



def index(request):
    context = {}
    return render(request, 'booktest/index.html', context)