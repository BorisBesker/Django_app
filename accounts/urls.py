from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name="login"),
    url(r'^logout/$', views.Logout.as_view(), name="logout"),
    url(r'^register/$', views.Register.as_view(), name="register"),
]
