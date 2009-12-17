from django.conf.urls.defaults import patterns

urlpatterns = patterns('repeatblock.views',
    (r'^$', 'repeatblock_example'),
)