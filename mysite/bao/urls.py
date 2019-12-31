from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.basic_ayasdi_apps, name="basic_ayasdi_apps"),
]