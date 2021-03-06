# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from  django.contrib.auth.models import User as AuthUser
from iptvresource.models import Vlan, MulticastIp
from device.models import Encoder
from channel.models import Channel
from agent.models import Agent

class ProfileState(models.Model):
    state = models.IntegerField(primary_key=True, blank=False, null=False)
    name = models.CharField(unique=True, max_length=10, blank=False, null=False)
    description = models.CharField(max_length=60, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'profile_state'
    def __str__(self):
        return u'%s '%(self.name)
        


class ProfileQuality(models.Model):
    id = models.AutoField(primary_key=True)
    quality = models.CharField(unique=True, max_length=45)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'profile_quality'
    def __str__(self):
        return u'%s '%(self.quality)


class GroupProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'group_profile'
    def __str__(self):
        return u'%s '%(self.name)



class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=60, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    profile_quality = models.ForeignKey('ProfileQuality', models.CASCADE)
    channel = models.ForeignKey(Channel, models.CASCADE)
    multicast_ip = models.ForeignKey(MulticastIp, models.CASCADE)
    vlan = models.ForeignKey(Vlan, models.CASCADE)
    is_original = models.BooleanField() 
    encoder = models.ForeignKey(Encoder, models.CASCADE)
    status = models.ForeignKey(ProfileState, models.CASCADE, default=1)

    class Meta:
        managed = True
        db_table = 'profile'
        unique_together = (('profile_quality', 'channel', 'multicast_ip'),)
    def __str__(self):
        return u'Channel %s - type %s - ip %s '%(self.channel, self.profile_quality, self.multicast_ip  )



class GroupProfileHasProfile(models.Model):
    id = models.AutoField(primary_key=True)
    group_profile = models.ForeignKey(GroupProfile, models.CASCADE)
    profile = models.ForeignKey(Profile, models.CASCADE)

    class Meta:
        managed = True  
        db_table = 'group_profile_has_profile'
        unique_together = (('profile', 'group_profile'),)
    def __str__(self):
        return u'Group %s has %s'%(self.group_profile, self.profile)

class EncoderInputProfile(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, models.CASCADE)
    encoder = models.ForeignKey(Encoder, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'encoder_input_profile'
        unique_together = (('encoder', 'profile'),)
    def __str__(self):
        return u'Encoder %s has profile %s '%(self.encoder, self.profile)

class Monitor(models.Model):
    id = models.AutoField(primary_key=True)
    status_signal = models.BooleanField() 
    status_video = models.BooleanField() 
    status_audio = models.BooleanField() 
    signal_monitor = models.BooleanField() 
    video_monitor = models.BooleanField() 
    audio_monitor = models.BooleanField() 
    is_enable = models.BooleanField() 
    date_update = models.DateTimeField(blank=True, null=True)
    agent = models.ForeignKey(Agent, models.CASCADE)
    profile = models.ForeignKey(Profile, models.CASCADE)
    status = models.ForeignKey(ProfileState, models.CASCADE, default=1)
    class Meta:
        managed = True
        db_table = 'monitor'
        unique_together = (('profile', 'agent'),)
    def __str__(self):
        return u'Monitor profile: %s on agent: %s'%(self.profile, self.agent)


class AgentHasGroupProfile(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(Agent, models.CASCADE)
    group_profile = models.ForeignKey(GroupProfile, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'agent_has_group_profile'
        unique_together = (('agent', 'group_profile'),)
    def __str__(self):
        return u'Agent: %s monitor group profile: %s'%(self.agent, self.group_profile)
