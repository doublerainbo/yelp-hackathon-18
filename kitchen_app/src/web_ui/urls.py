from django.conf.urls import patterns, url

from kitchen_app.web_ui import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)