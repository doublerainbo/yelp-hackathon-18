from django.conf.urls import patterns, url

from kitchen_app.src.api import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^create_request$', views.create_request, name='create_request'),
    url(r'^cancel_request$', views.cancel_request, name='cancel_request'),
    url(r'^ack_request$', views.ack_request, name='ack_request'),
    url(r'^fulfill_request$', views.fulfill_request, name='fulfill_request'),
    url(r'^current_requests$', views.current_requests, name='current_requests'),
    url(r'^available_items$', views.available_items, name='available_items'),
    url(r'^clear_database$', views.clear_database, name='clear_database'),
)