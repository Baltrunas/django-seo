from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^api/json/category/list/$', views.robots, name='robots'),
]
