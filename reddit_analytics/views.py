from django.shortcuts import render

from .models import Comment, Submission

# Create your views here.


def home(request):
    submissions = Submission.objects.all()
    comments = Comment.objects.all()
    context = {
        "submissions": submissions,
        "comments": comments,
    }
    return render(request, "reddit_analytics/home.html", context)
