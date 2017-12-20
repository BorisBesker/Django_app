from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views import View
from django.db.utils import OperationalError
from django.shortcuts import render


from google_maps.models import Location, DateVisited


class Welcome(LoginRequiredMixin, View):

    login_url = '/accounts/login/'
    template_name = 'google_maps/welcome.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'place': request.GET.get('place')})


class ListLocations(LoginRequiredMixin, View):

    login_url = '/accounts/login/'
    template_name = 'google_maps/locations.html'

    def post(self, request, *args, **kwargs):
        try:
            current_location, created = Location.objects.get_or_create(name=request.POST['place'])
        except OperationalError:
            return HttpResponseBadRequest()

        d1 = DateVisited(user=request.user, location=current_location)
        d1.save()

        return JsonResponse({'place': current_location.name})

    def get(self, request, *args, **kwargs):
        dict1 = {'Split': [1, 2, 4], 'Zagreb': [1, 4, 6]}

        return render(request, self.template_name, {'locations': dict1})

        #{'locations': dict1, 'place': 'Split'}
    #def get(self, request, *args, **kwargs):
    #    list1 = []
    #    dates = DateVisited.objects.filter(user=request.user).order_by('-location__name')
    #    for date in dates:

    #        list1.append(str(date.location) + '-' + str(date.date_visited) + '        ')

    #    return HttpResponse(list1)

