from django.conf.urls import url

from .views import Welcome, ListLocations

app_name = 'google_maps'
urlpatterns = [
    url(r'^location/$', ListLocations.as_view(), name='locations_list'),
    url(r'^welcome/$', Welcome.as_view(), name='welcome')
]
