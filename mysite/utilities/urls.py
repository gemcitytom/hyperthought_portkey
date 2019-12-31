from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.utility_apps, name="utility_apps"),
]