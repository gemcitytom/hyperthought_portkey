from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.thd_ops, name="thd_ops"),
]