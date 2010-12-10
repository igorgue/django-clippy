import os

from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    ('^', include('test_clippy.urls')),
)

urlpatterns += patterns('',
    (r'^flash/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.PROJECT_PATH, 'public/flash')}),
)
