from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #Do the work here...
    # response = "<h1>Hello, world!</h1>"

    # ... and return a response with its results
    # return HttpResponse(response)
    return render(request, 'users/home.html', {})

def detail(request):
    return HttpResponse("<h1>detail views!!</h1>")

def add(request):
    return HttpResponse("<h1>add views!!</h1>")