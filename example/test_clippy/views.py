"""
views.py - just a render to response to the template the shows the clippy thing
"""

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    """just renders the template"""
    repo_url = "git@github.com:igorgue/django-clippy.git"

    return render_to_response('index.html', {'repo_url': repo_url}, context_instance=RequestContext(request))
