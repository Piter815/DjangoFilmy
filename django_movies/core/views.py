from django.shortcuts import render
from django.http import HttpResponse
from core.models import Movies


def hello(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives':['beautiful','cruel','wonderful']},
    )

def movies(request):
    return render(
        request,
        template_name='movies.html',
        context={'movies': Movies.objects.all()},
    )