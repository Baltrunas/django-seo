from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^robots\.txt$', views.robots, name='robots'),
]
