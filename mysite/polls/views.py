from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 4c640b1f is the polls index.")