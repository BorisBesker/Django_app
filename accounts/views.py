from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView

from .forms import RegisterForm, UserForm


class Login(View):

    form_class = UserForm
    template_name = 'accounts/login.html'

    def get(self, request):
        """Handles the GET Http request

        If user is authenticated performs redirection, if not authenticated returns the associated
        template

        :param request:
        :return:
        """
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('google_maps:welcome'))
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        """Handles the POST Http request

        If form validation has passed loges the user, else returns the template with form errors

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect(reverse('google_maps:welcome'))

        return render(request, self.template_name, {'form': form})


class Register(View):

    form_class = RegisterForm
    template_name = 'accounts/registration.html'

    def get(self, request):
        """Handles the GET Http request

        If user is authenticated performs redirection, if not authenticated returns the associated
        template.

        :param request:
        :return:
        """
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('google_maps:welcome'))
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        """Handles the POST Http request

        If form validation has passed registers the user then loges the user, else returns the
        template with form errors

        :param request:
        :return:
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect(reverse('google_maps:welcome'))

        return render(request, self.template_name, {'form': form})


class Logout(LoginRequiredMixin, View):

    login_url = '/accounts/login/'

    def get(self, request):
        """Handles the GET Http request

        If user is not logged in redirects to 'login_url', if authenticated loges out the user in.

        :param request:
        :return:
        """
        logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))
