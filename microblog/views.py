from django.shortcuts import render
from microblog.models import Tweet

# Create your views here. Remember django views are controllers
def homepage(request):
    if request.method == "POST":
        Tweet.objects.create(
            text=request.POST["text"],
            user=request.user,
        )
    all_tweets = Tweet.objects.all()
    context = {
        'tweets': all_tweets,
    }
    return render(request, 'homepage.html', context)