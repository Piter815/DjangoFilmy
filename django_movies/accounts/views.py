from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from accounts.forms import SubmittableAuthenticationForm, SubmittablePasswordchangeForm
from django.contrib import messages

# Create your views here.
from django.urls import reverse_lazy


class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'forms.html'


class SubmittablePasswordchangeView(PasswordChangeView):
    form_class = SubmittablePasswordchangeForm
    template_name = 'forms.html'
    success_url = reverse_lazy('index')


class SuccessMessageLogoutView(LogoutView):
    def get_next_page(self):
        result = super().get_next_page()
        messages.success(self.request, 'Successfully logged out!')
        return result
