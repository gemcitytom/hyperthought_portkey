from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.adv_ayasdi_apps, name="adv_ayasdi_apps"),
]