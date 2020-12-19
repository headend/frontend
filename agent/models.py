# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from iptvresource.models import Vlan


class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    ip_control = models.CharField(unique=True, max_length=15)
    ip_receive_multicast = models.CharField(max_length=15, blank=True, null=True)
    cpu = models.SmallIntegerField(blank=True, null=True)
    ram = models.SmallIntegerField(blank=True, null=True)
    disk = models.SmallIntegerField(blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    is_monitor = models.BooleanField()
    is_alarm = models.BooleanField()
    signal_monitor = models.BooleanField()
    video_monitor = models.BooleanField()
    audio_monitor = models.BooleanField()
    run_thread   = models.IntegerField(blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    class Meta:
        managed = True
        db_table = 'agent'
    def __str__(self):
        return u'%s - %s'%(self.ip_control, self.location if self.location else "Plz set location")


class AgentHasVlan(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(Agent, models.CASCADE)
    vlan = models.ForeignKey(Vlan, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'agent_has_vlan'
        unique_together = (('vlan', 'agent'),)
    def __str__(self):
        return u'%s | Vlanid %s'%(self.agent,self.vlan.vlanid)


