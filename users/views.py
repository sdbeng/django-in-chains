from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse

from .models import User

# Create your views here.
def home(request):
    #Do the work here...
    # response = "<h1>Hello, world!</h1>"

    # ... and return a response with its results
    # return HttpResponse(response)
    # return render(request, 'users/home.html', {})
    context = {'name': 'Dani', 'tasks': ['breakfast time', 'ride bike', 'Go to work', 'hack pipenv projects', 'snack time', 'Watch favorite tv show','Go to bed']}
    return render(request, 'users/home.html', context)

def detail(request, user_id):
    # return HttpResponse("<h1>detail views!!</h1>")
    # context = {'header': 'This is my detail vieeeeeeeew!!'}

    # instead of a try-except block, i can use get_object_or_404 method
    user = get_object_or_404(User, user_id)
    context = {'user': User.objects.get(first_name='jane')}
    return render(request, 'users/detail.html', context)

def add(request):
    # return HttpResponse("<h1>add views!!</h1>")
    context = {'header': 'This is my add view!!'}

    return render(request, 'users/add.html', context)