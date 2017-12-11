from django.conf.urls import url

from .views import Welcome

app_name = 'google_maps'
urlpatterns = [
    url(r'^welcome/$', Welcome.as_view(), name='welcome'),
]

