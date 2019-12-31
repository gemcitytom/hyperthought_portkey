from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.thd_apps, name="thd_apps"),
]