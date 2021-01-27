from django.shortcuts import render
import time
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import loader
import logging
from .models import MonitorLogs
from agent.models import Agent
from channel.models import Channel
from iptvresource.models import MulticastIp
import json
from django.db.models import F
from utils import convert_seconds_to_day, caculate_distance
import datetime

def get_monitor_logs_object():
    result = None
    result = MonitorLogs.objects.values('id','agent_id','profile_id','monitor_id','channel_id','channel_name','multicast_ip','before_status','after_status','desc','date_create').order_by('-date_create')[:300]
    for monitor_log in result:
        if monitor_log['date_create']:
            monitor_log['distance'] = convert_seconds_to_day(caculate_distance(monitor_log['date_create']))
            monitor_log['date_create'] = monitor_log['date_create'].strftime("%Y/%m/%d %H:%M:%S")
        else:
            monitor_log['date_create'] = ""
    return result

def index(request):
    template = loader.get_template('monitor_logs/index.html')
    data = get_monitor_logs_object()
    agents = Agent.objects.values('id', 'ip_control', 'location').order_by('location', 'ip_control')
    channels = Channel.objects.values('id', 'name').order_by('-name')
    multicast_ips = MulticastIp.objects.values('id', 'ip').order_by('ip')
    context = {
        'data': data,
        'agents': agents,
        'channels': channels,
        'multicast_ips': multicast_ips
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
def reload_data(request):
    if request.method == "GET":
        data = get_monitor_logs_object()
        # print(json.dumps(data))
        return HttpResponse(json.dumps(data), status=200, content_type='application/json')
    else:
        return HttpResponse(500)

@csrf_exempt
def load_filter(request):
    if request.method == "POST":
        channel = request.POST.get('channel')
        agent = request.POST.get('agent')
        multiip = request.POST.get('multiip')
        print("Request from client:{0}-{1}-{2}".format(channel, agent, multiip))
        data = list(get_search_logs(channel, agent, multiip))
        print("search multiIP!")
        # print(data)
        return HttpResponse(json.dumps(data),status=200, content_type='application/json')
    return HttpResponse(500)

def get_search_logs(channel, agent, multiip):
    result = None
    if channel and agent and multiip:
        result = MonitorLogs.objects.extra(where=["channel_id='{0}' AND agent_id='{1}' AND multicast_ip='{2}'".format(channel, agent, multiip)]).values('id','agent_id','profile_id','monitor_id','channel_id','channel_name','multicast_ip','before_status','after_status','desc','date_create').order_by('-date_create')[:300]
    elif channel and agent and not multiip:
        result = MonitorLogs.objects.extra(where=["channel_id='{0}' AND agent_id='{1}'".format(channel, agent)]).values('id','agent_id','profile_id','monitor_id','channel_id','channel_name','multicast_ip','before_status','after_status','desc','date_create').order_by('-date_create')[:300]
    elif channel and multiip and not agent:
        result = MonitorLogs.objects.extra(where=["channel_id='{0}' AND multicast_ip='{1}'".format(channel, multiip)]).values('id','agent_id','profile_id','monitor_id','channel_id','channel_name','multicast_ip','before_status','after_status','desc','date_create').order_by('-date_create')[:300]
    elif channel and not agent and not multiip:
        result = MonitorLogs.objects.extra(where=["channel_id='{0}'".format(channel)]).values('id','agent_id','profile_id','monitor_id','channel_id','channel_name','multicast_ip','before_status','after_status','desc','date_create').order_by('-date_create')[:300]
    elif agent and multiip and not channel:
        result = MonitorLogs.objects.extra(where=["agent_id='{0}' AND multicast_ip='{1}'".format(agent, multiip)]).values('id','agent_id','profile_id','monitor_id','channel_id','channel_name','multicast_ip','before_status','after_status','desc','date_create').order_by('-date_create')[:300]
    elif agent and not multiip and not channel:
        result = MonitorLogs.objects.extra(where=["agent_id='{0}'".format(agent)]).values('id','agent_id','profile_id','monitor_id','channel_id','channel_name','multicast_ip','before_status','after_status','desc','date_create').order_by('-date_create')[:300]
    elif multiip and not agent and not channel:
        result = MonitorLogs.objects.extra(where=["multicast_ip='{0}'".format(multiip)]).values('id','agent_id','profile_id','monitor_id','channel_id','channel_name','multicast_ip','before_status','after_status','desc','date_create').order_by('-date_create')[:300]
    else:
        return result
    for monitor_log in result:
        if monitor_log['date_create']:
            monitor_log['distance'] = convert_seconds_to_day(caculate_distance(monitor_log['date_create']))
            monitor_log['date_create'] = monitor_log['date_create'].strftime("%Y/%m/%d %H:%M:%S")
        else:
            monitor_log['date_create'] = ""
    return result

