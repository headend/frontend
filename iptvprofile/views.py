from django.shortcuts import render
from django.core import serializers
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from iptvprofile.models import Monitor
from iptvprofile.models import Profile
from iptvprofile.models import ProfileQuality, ProfileState
from channel.models import Channel
from iptvresource.models import MulticastIp, Vlan
from device.models import Encoder
from agent.models import Agent
from django.db.models import F
import json
from utils import convert_seconds_to_day, caculate_distance

# Create your views here.
@csrf_exempt
def index(request):
    template = loader.get_template('iptvprofile/index.html')
    data = Monitor.objects.select_related('agent','profile').values('id','status','date_update',location=F('agent__location'),mulip=F('profile__multicast_ip__ip'),channel=F('profile__channel__name'),
    sigmonitor=F("signal_monitor"),vidmonitor=F('video_monitor'),vidstatus=F('status_video'),audmonitor=F('audio_monitor'), audstatus=F('status_audio'),isenable=F('is_enable'),
    quality=F('profile__profile_quality__quality'),
    ).order_by('status', '-date_update')
    for monitor in data:
        if monitor['date_update']:
            monitor['downtime'] = convert_seconds_to_day(caculate_distance(monitor['date_update'])) if not monitor['status'] else ''
            monitor['date_update'] = monitor['date_update'].strftime("%Y/%m/%d %H:%M:%S") if monitor['date_update'] else ''
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))
@csrf_exempt
def profile(request):
    template = loader.get_template('iptvprofile/profile.html')
    data = Profile.objects.values('id','desc',date_cr=F('date_create'),date_up=F('date_update'),quality=F('profile_quality__quality'), p_channel=F('channel__name'), mulip=F('multicast_ip__ip'),
    p_vlan=F('vlan__vlan_provider__name'), p_status=F('status__name'))
    # print(data)
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))
@csrf_exempt
def getId(request):
    if request.method == "GET":
        data= list(Monitor.objects.values('id'))
        # print(serializers.serialize('json',data))
        return JsonResponse(data, safe=False)
        # return HttpResponse('sdfdf',status=200)
    else:
        return HttpResponse(status=500)
@csrf_exempt
def updateStatus(request):
    if request.method == "GET":
        data = list(Monitor.objects.select_related('agent','profile').values('id','status','date_update',location=F('agent__location'),mulip=F('profile__multicast_ip__ip'),channel=F('profile__channel__name'),
        sigmonitor=F("signal_monitor"),vidmonitor=F('video_monitor'),vidstatus=F('status_video'),audmonitor=F('audio_monitor'), audstatus=F('status_audio'),isenable=F('is_enable'),
        quality=F('profile__profile_quality__quality'),
        ).order_by('status', '-date_update'))
        for monitor in data:
            if monitor['date_update']:
                monitor['downtime'] = convert_seconds_to_day(caculate_distance(monitor['date_update'])) if not monitor['status'] else ''
                monitor['date_update'] = monitor['date_update'].strftime("%Y/%m/%d %H:%M:%S") if monitor['date_update'] else ''
        return HttpResponse(json.dumps(data),status=200,content_type="application/json")
    else:
        return HttpResponse(status=500)
    # return JsonResponse(data=data, safe=False)
@csrf_exempt
def getDataForAdd(request):
    if request.method == "GET":
        data = {
            "Quality": '',
            "Channel": '',
            "MulCastIp": '',
            "Vlan": '',
            "Encoder": '',
            "State": ''
        }
        try:
            proQua = list(ProfileQuality.objects.values('id','quality'))
            channle = list(Channel.objects.values('id','name'))
            mulip = list(MulticastIp.objects.values('id','ip'))
            vlan = list(Vlan.objects.values('id','vlanid'))
            encoder = list(Encoder.objects.values('id','name'))
            proState = list(ProfileState.objects.values('state', 'name'))
            data = {
                "Quality": proQua,
                "Channel": channle,
                "MulCastIp": mulip,
                "Vlan": vlan,
                "Encoder": encoder,
                "State": proState
            }
        except Exception as e:
            print(e)
        print(json.dumps(data))
        return HttpResponse(json.dumps(data), status=200, content_type="application/json")
    return HttpResponse(status=404)
@csrf_exempt
def addNewProfile(request):
    if request.method == "POST":
        print(request.POST.get("quality"))
        quality = ProfileQuality.objects.get(id=request.POST.get("quality"))
        print(quality)
        channel = Channel.objects.get(id=request.POST.get('channel'))
        multicastip = MulticastIp.objects.get(id=request.POST.get('mulcast'))
        vlan = Vlan.objects.get(id=request.POST.get('vlan'))
        encoder = Encoder.objects.get(id=request.POST.get('encoder'))
        status = ProfileState.objects.get(state=request.POST.get('status'))
        try:
            record = Profile(profile_quality= quality, channel=channel, multicast_ip=multicastip, vlan=vlan,
                             encoder=encoder, status=status, is_original=True)
            record.save(force_insert=True)
            # print(Profile.objects.get(channel=channel))
            return HttpResponse(status=200)
        except Exception as e:
            print(e)
            return HttpResponse("Profile have existed!", status=406, content_type="application/text")
    return HttpResponse(status=404)
@csrf_exempt
def deleteProfile(request, id):
    if request.method == "DELETE":
        print(type(id))
        try:
            agent = Profile.objects.get(id=id)
            agent.delete()
            msg = "Profile {0} was deleted".format(id)
            return HttpResponse(msg,status=201, content_type="application/text")
        except Exception as e:
            print (e)
            return HttpResponse("Have Error", status=500)
    return HttpResponse("Have Error",status=500)
@csrf_exempt
def getData4AddMonitor(request):
    if request.method == "GET":
        data = {
            "Agent":'',
            "Profile":'',
            "Status":'',
        }
        try:
            agent=list(Agent.objects.values('id','location', ip =F('ip_control')))
            profile = list(Profile.objects.values('id',channelname=F('channel__name'),quality=F('profile_quality__quality')))
            proState = list(ProfileState.objects.values('state', 'name'))
            data={
                "Agent": agent,
                "Profile": profile,
                "Status": proState,
            }
        except Exception as e:
            print(e)
        print(data)
        return HttpResponse(json.dumps(data), status=200, content_type='application/json')
    return HttpResponse(status=404)

@csrf_exempt
def addNewMonitor(request):
    if request.method == "POST":
        agent = Agent.objects.get(id=request.POST.get('agent'))
        profile = Profile.objects.get(id=request.POST.get('profile'))
        status = ProfileState.objects.get(state=request.POST.get('status'))
        enable = request.POST.get('enable')
        video = request.POST.get('video')
        audio = request.POST.get('audio')
        signal = request.POST.get('signal')
        try:
            record = Monitor(signal_monitor=signal, video_monitor=video, agent=agent, profile=profile, status=status,
                             is_enable=enable, audio_monitor=audio, status_signal=False, status_audio=False, status_video=False)
            record.save(force_insert=True)
            return HttpResponse(status=200)
        except Exception as e:
            print(e)
            return HttpResponse("Monitor have existed!", status=404, content_type="application/text")
    return HttpResponse("Have error!",status=404, content_type="application/text")
@csrf_exempt
def deleteMontior(request, id):
    if request.method == "DELETE":
        print(type(id))
        try:
            agent = Monitor.objects.get(id=id)
            agent.delete()
            msg = "Monitor was deleted".format(id)
            return HttpResponse(msg,status=201, content_type="application/text")
        except Exception as e:
            print (e)
            return HttpResponse("Have Error", status=500)
    return HttpResponse("Have Error",status=500)
