from concurrent.futures._base import LOGGER

from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponse, request
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from core.models import Movies
from core.forms import MovieForm


def hello(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives':['beautiful','cruel','wonderful']},
    )

class MovieListView(ListView):
    template_name = 'movies.html'
    model = Movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_list'] = Movies.objects.filter(genre__age_limit__lte=1)
        return context


class MovieCreateView(CreateView):
    title = 'Add Movie'
    template_name = 'forms.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

    # form = MovieForm(request.POST)
    # if form.is_valid():
    #     form.save()


class MovieUpdateView(UpdateView):
    title = 'Add Movie'
    model = Movies
    template_name = 'forms.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieDeleteView(DeleteView):
    model = Movies
    template_name = 'movies_confirm_delete.html'
    # form_class = MovieForm
    success_url = reverse_lazy('movie_create')

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)

    # def movies(request):
#     return render(
#         request,
#         template_name='movies.html',
#         context={'movies': Movies.objects.all()},
#     )


class IndexView(MovieListView):
    template_name = 'index.html'