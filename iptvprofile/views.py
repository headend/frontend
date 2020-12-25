from django.shortcuts import render
from django.core import serializers
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from iptvprofile.models import Monitor

# Create your views here.
def index(request):
    template = loader.get_template('iptvprofile/index.html')
    data = Monitor.objects.select_related('agent','profile')
    print(serializers.serialize('json',data))
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))