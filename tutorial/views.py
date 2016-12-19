from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
# Create your views here.


def homepage(request):
    return render(request, 'music/home.html')
