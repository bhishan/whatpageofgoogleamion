from django.conf.urls import patterns, include, url

urlpatterns = patterns('whatpageofsearchamion.views', (r'^$', 'archive'),(r'^create/','create_search'),)
