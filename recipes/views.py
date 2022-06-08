from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('hello amigos')


def contact(request):
    return HttpResponse('contact page')


def about(request):
    return HttpResponse('about page')
