from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import OperationalError
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views import View

from google_maps.models import Location, DateVisited


class Welcome(LoginRequiredMixin, View):

    login_url = '/accounts/login/'
    template_name = 'google_maps/welcome.html'

    def get(self, request):
        """Handles the GET Http request

        If user is not logged in redirects to 'login_url', else renders the template.

        :param request:
        :return:
        """
        return render(request, self.template_name, {'place': request.GET.get('place')})


class ListLocations(LoginRequiredMixin, View):

    login_url = '/accounts/login/'
    template_name = 'google_maps/locations.html'

    def post(self, request):
        """Handles the POST Http request

        If user is not logged in redirects to 'login_url', else checks if the current location
        exists in database (ifnot, saves it) then associates it with the current user and returns
        Json response for further processing. In case of operational error, e.g. saving location
        with Chinese letters, raises a HttpResponseBadRequest.

        :param request:
        :return:
        """
        try:
            current_location, created = Location.objects.get_or_create(name=request.POST['place'])
        except OperationalError:
            return HttpResponseBadRequest()
        date_visited_record = DateVisited(user=request.user, location=current_location)
        date_visited_record.save()
        return JsonResponse({'place': current_location.name})

    def get(self, request):
        """Handles the GET Http request

        If user is not logged in redirects to 'login_url', else renders the template
        with user-locations records.

        :param request:
        :return:
        """
        dates = DateVisited.objects.filter(user=request.user).prefetch_related('location').\
            order_by('-date_visited')
        return render(request, self.template_name, {'dates': dates})
