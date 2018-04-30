from django.conf.urls import include, url
from . import views



urlpatterns = [
	url(r'^projectinfo/', views.projectinfo, name='projectinfo'),
	url(r'^team/', views.team, name='team'),
	url(r'^scenario1/', views.scenario1, name='scenario1'),
	url(r'^scenario2/', views.scenario2, name='scenario2'),
	url(r'^scenario3/', views.scenario3, name='scenario3'),
	url(r'^scenario4/', views.scenario4, name='scenario4'),
	url(r'^home/$', views.Home, name='home'),
	url(r'^git/$', views.git, name='git'),
	url(r'^$', views.Home, name='home'),
]