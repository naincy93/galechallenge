from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'views.handle_home'),
                       url(r'^detail/(?P<article_id>.*)/$', 'views.handle_detail')
)
