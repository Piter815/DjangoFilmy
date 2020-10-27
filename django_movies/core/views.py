from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView
from core.models import Movies
from core.forms import MovieForm


def hello(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives':['beautiful','cruel','wonderful']},
    )


class MovieView(ListView):
    template_name = 'movies.html'
    model = Movies

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['movie_list'] = Movies.objects.filter(genre__age_limit__lte=1)
        return context

class MovieCreateView(FormView):
    template_name = 'forms.html'
    form_class = MovieForm


# def movies(request):
#     return render(
#         request,
#         template_name='movies.html',
#         context={'movies': Movies.objects.all()},
#     )