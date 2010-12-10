import os

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('test_clippy.views',
    url(r'^$', 'index', name="index"),
)

urlpatterns += patterns('',
    (r'^flash/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'public/flash')}),
)
