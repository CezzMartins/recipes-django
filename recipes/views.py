from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/home.html')


def contact(request):
    return HttpResponse('contact page')


def about(request):
    return HttpResponse('about page')
