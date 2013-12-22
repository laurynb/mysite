from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',

      url(r'^$', 'app.views.common.home', name='home'),
      url(r'^about/$', 'app.views.common.about', name='about'),
      url(r'^projects/$', 'app.views.common.projects', name='projects'),
      url(r'^blog/$', 'app.views.common.about', name='blog'),
      url(r'^contact/$', 'app.views.common.contact', name='contact'),

)
