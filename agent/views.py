from django.shortcuts import render
import time
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import logging
from datetime import timedelta
from agent.models import Agent
from iptv_frontend.config import WORKER
import json


def index(request):
    template = loader.get_template('agents/index.html')
    data = Agent.objects.all()
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def updateAgent(request):
    if request.method == 'POST':
        try:
            agent = Agent.objects.get(id=request.POST.get('id'))
            data= {    
            "agent_id": agent.id,
            "control_id": None,
            "TunnelData": ""} 
            respo = {}
            if agent.is_monitor != request.POST.get('monitor'):
                respo["monitor"] = pushWorker(data=data,host=WORKER["host"],uri=WORKER["worker"][request.POST.get('monitor')])
            else:
                respo["monitor"] = "No change"
            if agent.signal_monitor == request.POST.get('signal'):
                respo["signal"] = pushWorker(data=data,host=WORKER["host"],uri=WORKER["signal"][request.POST.get('signal')]) 
            else:
                respo["signal"] = "No change"
            if agent.video_monitor == request.POST.get('video'):
                respo["video"] = pushWorker(data=data,host=WORKER["host"],uri=WORKER["video"][request.POST.get('video')])
            else:
                respo["video"] = "No change"
            if agent.audio_monitor == request.POST.get('audio'):
                respo["audio"] = pushWorker(data=data,host=WORKER["host"],uri=WORKER["audio"][request.POST.get('audio')])
            else:
                respo["audio"] = "No change"
            agent.status = request.POST.get('status', '')
            agent.location = request.POST.get('location', '')
            agent.is_alarm = request.POST.get('alarm', '')
            agent.signal_monitor = request.POST.get('signal', '')
            agent.video_monitor = request.POST.get('video', '')
            agent.audio_monitor = request.POST.get('audio', '')
            agent.run_thread = request.POST.get('thread', 0)
            agent.save()
            print("is monitor {0}".format(respo["monitor"]))
            return HttpResponse("update ok",status=200, content_type="application/text")
        except Exception as e:
            print(e)
            return HttpResponse(status=500)
    else:
        return HttpResponse(status=400)

def pushWorker(data,host,uri):
    import requests, json
    url = "{0}{1}".format(host, uri)
    print (url)
    try:
        res = requests.post(url=url, data=json.dumps(data))
        if res.status_code ==200:
            print(res.content)
            return res.status_code
        else:
            return res.status_code
    except Exception as e:
        print(e)
        return 500
@csrf_exempt
def deleteAgent(request, id):
    if request.method == "DELETE":
        print(type(id))
        try:
            agent = Agent.objects.get(id=id)
            agent.delete()
            msg = "Deleted agent {0}".format(id)
            return HttpResponse(msg,status=201)
        except Exception as e:
            print (e)
            return HttpResponse("Have Error", status=500)
    return HttpResponse("Have Error",status=500)
# Create your views here.
