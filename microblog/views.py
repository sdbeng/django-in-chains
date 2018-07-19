from django.shortcuts import render
from microblog.models import Tweet

# Create your views here.
def homepage(request):
    all_tweets = Tweet.objects.all()
    context = {
        'tweets': all_tweets,
    }
    return render(request, 'homepage.html', context)