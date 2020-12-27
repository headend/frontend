from django.shortcuts import render
from django.core import serializers
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from iptvprofile.models import Monitor
from django.db.models import F
import json

# Create your views here.
def index(request):
    template = loader.get_template('iptvprofile/index.html')
    data = Monitor.objects.select_related('agent','profile').values('id','status',location=F('agent__location'),mulip=F('profile__multicast_ip__ip'),channel=F('profile__channel__name'),
    sigmonitor=F("signal_monitor"),vidmonitor=F('video_monitor'),vidstatus=F('status_video'),audmonitor=F('audio_monitor'), audstatus=F('status_audio'),isenable=F('is_enable'),
    quality=F('profile__profile_quality__quality'),
    )
    # data = list(data)
    print(data)
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))

def getId(request):
    if request.method == "GET":
        print("aaa")
        data= list(Monitor.objects.values('id'))
        # print(serializers.serialize('json',data))
        return JsonResponse(data, safe=False)
        # return HttpResponse('sdfdf',status=200)
    else:
        return HttpResponse(status=500)

def updateStatus(request):
    if request.method == "GET":
        data = list(Monitor.objects.select_related('agent','profile').values('id','status',location=F('agent__location'),mulip=F('profile__multicast_ip__ip'),channel=F('profile__channel__name'),
        sigmonitor=F("signal_monitor"),vidmonitor=F('video_monitor'),vidstatus=F('status_video'),audmonitor=F('audio_monitor'), audstatus=F('status_audio'),isenable=F('is_enable'),
        quality=F('profile__profile_quality__quality'),
        ))
        return HttpResponse(json.dumps(data),status=200,content_type="application/json")
    else:
        return HttpResponse(status=500)
    # return JsonResponse(data=data, safe=False)