from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives':['beautiful','cruel','wonderful']},
    )