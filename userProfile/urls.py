from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.profile_list, name='list'),
    url(r'^create/$', views.profile_create, name='create'),
    url(r'^(?P<username>[-\w]+)/$', views.profile_detail, name='detail'),
    url(r'^(?P<username>[-\w]+)/edit/$', views.profile_update, name='update'),
	url(r'^(?P<username>[-\w]+)/delete/$', views.profile_delete, name='delete'),
]