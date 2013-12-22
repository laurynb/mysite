from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = patterns('',
    url(r'^mysite/', include('common.urls')),
    url(r'^$', 'app.views.common.home', name='home'),

)
