from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',

      url(r'^$', 'common.views.home', name='home'),
      url(r'^about/$', 'common.views.about', name='about'),
      url(r'^projects/$', 'common.views.projects', name='projects'),
      url(r'^blog/$', 'common.views.about', name='blog'),
      url(r'^contact/$', 'common.views.contact', name='contact'),

)
