from django.http import HttpResponse
from django.shortcuts import render







def indexs(request):
    return render(request, 'index/index.html')