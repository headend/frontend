# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from  django.contrib.auth.models import User as AuthUser


class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    ip_control = models.CharField(unique=True, max_length=15)
    ip_receive_multicast = models.CharField(max_length=15, blank=True, null=True)
    cpu = models.SmallIntegerField(blank=True, null=True)
    ram = models.SmallIntegerField(blank=True, null=True)
    disk = models.SmallIntegerField(blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    is_monitor = models.IntegerField(blank=True, null=True)
    is_alarm = models.IntegerField(blank=True, null=True)
    signal_monitor = models.IntegerField(blank=True, null=True)
    video_monitor = models.IntegerField(blank=True, null=True)
    audio_monitor = models.IntegerField(blank=True, null=True)
    run_thread = models.IntegerField(blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'agent'


class AgentHasGroupProfile(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(Agent, models.CASCADE)
    group_profile = models.ForeignKey('GroupProfile', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'agent_has_group_profile'
        unique_together = (('agent', 'group_profile'),)


class AgentHasVlan(models.Model):
    id = models.AutoField(primary_key=True)
    agent = models.ForeignKey(Agent, models.CASCADE)
    vlan = models.ForeignKey('Vlan', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'agent_has_vlan'
        unique_together = (('vlan', 'agent'),)


class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'channel'


class Encoder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    ip = models.CharField(unique=True, max_length=45, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    hardware = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    enviroment = models.ForeignKey('Enviroment', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'encoder'


class EncoderHasVlan(models.Model):
    id = models.AutoField(primary_key=True)
    vlan = models.ForeignKey('Vlan', models.CASCADE)
    encoder = models.ForeignKey(Encoder, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'encoder_has_vlan'
        unique_together = (('vlan', 'encoder'),)


class EncoderInputProfile(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey('Profile', models.CASCADE)
    encoder = models.ForeignKey(Encoder, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'encoder_input_profile'
        unique_together = (('encoder', 'profile'),)


class Enviroment(models.Model):
    name = models.CharField(unique=True, max_length=30)
    desc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enviroment'


class GroupChannel(models.Model):
    name = models.CharField(unique=True, max_length=30, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'group_channel'


class GroupChannelHasChannel(models.Model):
    group_channel = models.ForeignKey(GroupChannel, models.CASCADE)
    channel = models.ForeignKey(Channel, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'group_channel_has_channel'
        unique_together = (('channel', 'group_channel'),)


class GroupProfile(models.Model):
    name = models.CharField(unique=True, max_length=30)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'group_profile'


class GroupProfileHasProfile(models.Model):
    group_profile = models.ForeignKey(GroupProfile, models.CASCADE)
    profile = models.ForeignKey('Profile', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'group_profile_has_profile'
        unique_together = (('profile', 'group_profile'),)


class Monitor(models.Model):
    status_signal = models.IntegerField(blank=True, null=True)
    status_video = models.IntegerField(blank=True, null=True)
    status_audio = models.IntegerField(blank=True, null=True)
    signal_monitor = models.IntegerField(blank=True, null=True)
    video_monitor = models.IntegerField(blank=True, null=True)
    audio_monitor = models.IntegerField(blank=True, null=True)
    is_enable = models.IntegerField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    agent = models.ForeignKey(Agent, models.CASCADE)
    profile = models.ForeignKey('Profile', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'monitor'
        unique_together = (('profile', 'agent'),)


class MulticastIp(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(unique=True, max_length=15, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'multicast_ip'


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    desc = models.CharField(max_length=60, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    profile_quality = models.ForeignKey('ProfileQuality', models.CASCADE)
    channel = models.ForeignKey(Channel, models.CASCADE)
    multicast_ip = models.ForeignKey(MulticastIp, models.CASCADE)
    vlan = models.ForeignKey('Vlan', models.CASCADE)
    is_original = models.IntegerField()
    encoder = models.ForeignKey(Encoder, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'profile'
        unique_together = (('profile_quality', 'channel', 'multicast_ip'),)


class ProfileQuality(models.Model):
    id = models.AutoField(primary_key=True)
    quality = models.CharField(unique=True, max_length=45)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'profile_quality'


class SatelliteDishe(models.Model):
    name = models.CharField(unique=True, max_length=45)
    diameter = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    env = models.ForeignKey(Enviroment, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'satellite_dishe'
        unique_together = (('id', 'env'),)


class SatelliteDisheHasMulticastIp(models.Model):
    satellite_dishe = models.ForeignKey(SatelliteDishe, models.CASCADE)
    multicast_ip = models.ForeignKey(MulticastIp, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'satellite_dishe_has_multicast_ip'
        unique_together = (('multicast_ip', 'satellite_dishe'),)



class UserHasMulticastIp(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)
    multicast_ip = models.ForeignKey(MulticastIp, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'user_has_multicast_ip'
        unique_together = (('multicast_ip', 'user'),)


class Vlan(models.Model):
    id = models.AutoField(primary_key=True)
    vlanid = models.CharField(max_length=30)
    desc = models.CharField(max_length=60, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    env = models.ForeignKey(Enviroment, models.CASCADE)
    vlan_provider = models.ForeignKey('VlanProvider', models.CASCADE)

    class Meta:
        managed = True
        db_table = 'vlan'
        unique_together = (('vlan_provider', 'env', 'vlanid'),)


class VlanProvider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    address = models.CharField(max_length=60, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vlan_provider'
