from django.conf.urls.defaults import patterns

urlpatterns = patterns('repeatblock.views',
    (r'^$', 'repeatblock_example'),
    (r'^2/$', 'repeatblock_example_2'),
)