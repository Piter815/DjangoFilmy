
from core.views import MovieView

class IndexView(MovieView):
    template_name = 'index.html'
    title = 'Welcome to Django Movies!'