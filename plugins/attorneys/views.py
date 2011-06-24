from django.conf import settings
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404

from base.http import Http403
from site_settings.utils import get_setting
from perms.utils import has_perm
from attorneys.models import Attorney

def index(request, template_name='attorneys/index.html'):
    attorneys = Attorney.objects.order_by('create_dt')
    
    return render_to_response(template_name, 
        {
            'attorneys':attorneys,
        },
        context_instance=RequestContext(request))

def search(request, template_name='attorneys/search.html'):
    category = request.GET.get('category', None)
    q = request.GET.get('q', None)
    
    attorneys = Attorney.objects.search(query=q, user=request.user)
    
    if category:
        attorneys = attorneys.filter(category=category)
    
    return render_to_response(template_name, 
        {
            'attorneys':attorneys,
        },
        context_instance=RequestContext(request))

def detail(request, slug=None, template_name='attorneys/detail.html'):
    attorney = get_object_or_404(Attorney, slug=slug)
    
    if not has_perm(request.user, 'attorneys.view_attorney', attorney):
        raise Http403
    
    return render_to_response(template_name,
        {
            'attorney': attorney,
        },
        context_instance=RequestContext(request))
        
