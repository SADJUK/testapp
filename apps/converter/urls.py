from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^converter/$', 'converter.views.upload_file'),
    url(r'^converter/(?P<filename>(.*\.(json|xml|csv|JSON|CSV|XML)))$', 'converter.views.return_file'),
)
