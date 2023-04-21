from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'
