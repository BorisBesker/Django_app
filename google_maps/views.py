from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class Welcome(LoginRequiredMixin, TemplateView):

    login_url = '/accounts/login/'
    template_name = 'google_maps/welcome.html'
