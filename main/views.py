from django.shortcuts import render
from  django.http  import HttpResponse

def indexh(request):
    return render(request, 'index.html')