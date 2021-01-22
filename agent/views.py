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
from django.db.models import F 
from utils import convert_seconds_to_day, caculate_distance



def index(request):
    template = loader.get_template('agents/index.html')
    data = Agent.objects.all().order_by('-date_update')
    for agent in data:
        if not agent.status:
            agent.downtime = convert_seconds_to_day(caculate_distance(agent.date_update))
        else:
            agent.downtime = ""
        agent.version = agent.version if agent.version else ""
        agent.date_update = agent.date_update.strftime("%Y/%m/%d %H:%M:%S") if agent.date_update else ''
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def updateAgent(request):
    if request.method == 'POST':
        try:
            agent_id = request.POST.get('id')
            data= {    
            "agent_id": agent_id,
            "control_id": None,
            "TunnelData": ""} 
            respo = {'monitor':{'msg':'No change'}, 'signal':{'msg':'No change'}, 'audio':{'msg':'No change'}, 'video':{'msg': 'No change'}}
            is_monitor = True if agent.is_monitor else False
            if is_monitor != bool(int(request.POST.get('monitor'))):
                tmp = pushWorker(data=data,host=WORKER["host"],uri=WORKER["worker"][request.POST.get('monitor')])
                try:
                    tmp =json.loads(tmp)
                    # print(tmp['return_code'])
                    if tmp['return_code'] == 1:
                        respo["monitor"]["msg"]= "Successed"
                    else:
                        respo['monitor']['msg'] = tmp['return_message']
                except Exception as e:
                    respo["monitor"]["msg"]= "Have error"
               # print(respo)
            signal_monitor = True if agent.signal_monitor else False
            if signal_monitor != bool(int(request.POST.get('signal'))):
                tmp = pushWorker(data=data,host=WORKER["host"],uri=WORKER["signal"][request.POST.get('signal')]) 
                try:
                    tmp =json.loads(tmp)
                    # print("signal {0}".format(tmp))
                    if tmp['return_code'] == 1:
                        respo["signal"]["msg"]= "Successed"
                    else:

                        respo["signal"]["msg"]= tmp['return_message']
                except Exception as e:
                    respo["signal"]["msg"]= "Have error"
            video_monitor = True if agent.video_monitor else False
            if video_monitor != bool(int(request.POST.get('video'))):
                tmp = pushWorker(data=data,host=WORKER["host"],uri=WORKER["video"][request.POST.get('video')])
                try:
                    tmp =json.loads(tmp)
                    # print("video {0}".format(tmp))
                    if tmp['return_code'] == 1:
                        respo['video']['msg'] = "Successed"
                    else:
                        respo["video"]["msg"]= tmp['return_message']
                except Exception as e:
                    respo["video"]["msg"]= "Have error"
            audio_monitor = True if agent.audio_monitor else False
            if audio_monitor != bool(int(request.POST.get('audio'))):

                tmp = pushWorker(data=data,host=WORKER["host"],uri=WORKER["audio"][request.POST.get('audio')])
                try:
                    tmp =json.loads(tmp)
                    if tmp['return_code'] == 1:
                        respo['audio']['msg'] = "Successed"
                    else:
                        respo["audio"]["msg"]= tmp['return_message']
                except Exception as e:
                    respo["audio"]["msg"]= "Have error"
            # agent.status = request.POST.get('status', '')
            agent = Agent.objects.get(agent_id)
            agent.location = request.POST.get('location', '')
            # agent.is_alarm = request.POST.get('alarm', '')
            # agent.signal_monitor = request.POST.get('signal', '')
            # agent.video_monitor = request.POST.get('video', '')
            # agent.audio_monitor = request.POST.get('audio', '')
            # agent.run_thread = request.POST.get('thread', 0)
            agent.save()
            # print("is monitor {0}".format(respo["monitor"]))
            return HttpResponse(json.dumps(respo), status=200, content_type="application/json")
        except Exception as e:
            print(e)
            return HttpResponse(status=500)
    else:
        return HttpResponse(status=400)

def pushWorker(data,host,uri):
    import requests, json
    url = "{0}{1}".format(host, uri)
    # print (url)
    try:
        res = requests.post(url=url, data=json.dumps(data))
        if res.status_code ==200:
            return res.content
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
def updateStatus(request):
    if request.method == "GET":
        data = list(Agent.objects.values('id','location','status','date_update','version',ip=F('ip_control'),ismonitor=F('is_monitor'), sigmonitor=F('signal_monitor'),vidmonitor=F('video_monitor'),audmonitor=F('audio_monitor'),thread=F('run_thread')))
        # print(json.dumps(data))
        for agent in data:
            agent['downtime'] = convert_seconds_to_day(caculate_distance(agent['date_update'])) if not agent['status'] else ''
            agent['date_update'] = agent['date_update'].strftime("%Y/%m/%d %H:%M:%S")
        return HttpResponse(json.dumps(data), status=200, content_type='application/json')
    else:
        return HttpResponse(500)
