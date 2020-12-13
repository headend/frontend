import time
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import logging
from datetime import timedelta


def index(request):
    template = loader.get_template('servers/index.html')
    data = None
    rc= None
    msg = ""
    context = {
        'data': data,
        'rc': rc,
        'msg': msg,
    }
    return HttpResponse(template.render(context, request))
