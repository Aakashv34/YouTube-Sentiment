from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .youtube_api import get_comments
from .sentiment import analyze_sentiment
import re


def index(request):
    return render(request, 'index.html')


def analyze(request):

    if request.method == "POST":

        url = request.POST['url']

        video_id = re.findall(r"v=([^&]+)", url)[0]

        comments = get_comments(video_id)

        results, pos, neg, neu = analyze_sentiment(comments)

        context = {
            "results": results,
            "positive": pos,
            "negative": neg,
            "neutral": neu
        }

        return render(request, 'result.html', context)