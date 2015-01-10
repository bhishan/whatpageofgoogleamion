#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns

urlpatterns = patterns('whatpageofsearchamion.views', (r'^$', 'archive'),(r'^create/','create_search'),)
