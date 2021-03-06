from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request, template_name='home/home.html'):
    context = {}
    if request.user.is_authenticated():
        pass
        #return HttpResponseRedirect(reverse('', kwargs={}))
    return render_to_response(template_name, context, context_instance=RequestContext(request))
