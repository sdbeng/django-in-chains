from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #Do the work here...
    # response = "<h1>Hello, world!</h1>"

    # ... and return a response with its results
    # return HttpResponse(response)
    # return render(request, 'users/home.html', {})
    context = {'name': 'Dani', 'tasks': ['breakfast time', 'ride bike', 'Go to work', 'hack pipenv projects', 'snack time', 'Watch favorite tv show','Go to bed']}
    return render(request, 'users/home.html', context)

def detail(request):
    # return HttpResponse("<h1>detail views!!</h1>")
    context = {'header': 'This is my detail vieeeeeeeew!!'}
    return render(request, 'users/detail.html', context)

def add(request):
    # return HttpResponse("<h1>add views!!</h1>")
    context = {'header': 'This is my add view!!'}

    return render(request, 'users/add.html', context)