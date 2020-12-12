# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agent(models.Model):
    ip_control = models.CharField(primary_key=True, max_length=15)
    ip_multicast = models.CharField(max_length=15, blank=True, null=True)
    cpu = models.SmallIntegerField(blank=True, null=True)
    ram = models.SmallIntegerField(blank=True, null=True)
    disk = models.SmallIntegerField(blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    monitor = models.IntegerField(blank=True, null=True)
    alarm = models.IntegerField(blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'agent'


class AgentHasVlan(models.Model):
    agent_ip_control = models.ForeignKey(Agent, models.DO_NOTHING, db_column='agent_ip_control', primary_key=True)
    vlan = models.ForeignKey('Vlan', models.DO_NOTHING)
    vlan_env = models.ForeignKey('Vlan', models.DO_NOTHING, db_column='vlan_env')
    vlan_provider = models.ForeignKey('Vlan', models.DO_NOTHING, db_column='vlan_provider')

    class Meta:
        managed = True
        db_table = 'agent_has_vlan'
        unique_together = (('agent_ip_control', 'vlan', 'vlan_env', 'vlan_provider'),)


class Channel(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    group = models.ForeignKey('GroupChannel', models.DO_NOTHING, db_column='group', blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'channel'


class Encoder(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    ip = models.CharField(unique=True, max_length=45, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    hardware = models.CharField(max_length=45, blank=True, null=True)
    env = models.ForeignKey('Env', models.DO_NOTHING, db_column='env', blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    date_create = models.CharField(max_length=45, blank=True, null=True)
    date_update = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'encoder'


class EncoderHasProfile(models.Model):
    encoder_name = models.ForeignKey(Encoder, models.DO_NOTHING, db_column='encoder_name', primary_key=True)
    profile_channel = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_channel')
    profile_quality = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_quality')
    profile_env = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_env')

    class Meta:
        managed = True
        db_table = 'encoder_has_profile'
        unique_together = (('encoder_name', 'profile_channel', 'profile_quality', 'profile_env'),)


class EncoderHasVlan(models.Model):
    encoder_name = models.ForeignKey(Encoder, models.DO_NOTHING, db_column='encoder_name', primary_key=True)
    vlan = models.ForeignKey('Vlan', models.DO_NOTHING)
    vlan_env = models.ForeignKey('Vlan', models.DO_NOTHING, db_column='vlan_env')
    vlan_provider = models.ForeignKey('Vlan', models.DO_NOTHING, db_column='vlan_provider')

    class Meta:
        managed = True
        db_table = 'encoder_has_vlan'
        unique_together = (('encoder_name', 'vlan', 'vlan_env', 'vlan_provider'),)


class Env(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    desc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'env'


class GroupChannel(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'group_channel'


class GroupProfile(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'group_profile'


class GroupProfileHasProfile(models.Model):
    group_profile_name = models.ForeignKey(GroupProfile, models.DO_NOTHING, db_column='group_profile_name', primary_key=True)
    profile_channel = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_channel')
    profile_quality = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_quality')
    profile_env = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_env')

    class Meta:
        managed = True
        db_table = 'group_profile_has_profile'
        unique_together = (('group_profile_name', 'profile_channel', 'profile_quality', 'profile_env'),)


class Monitor(models.Model):
    agent_ip_control = models.ForeignKey(Agent, models.DO_NOTHING, db_column='agent_ip_control', primary_key=True)
    profile_channel = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_channel')
    profile_quality = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_quality')
    profile_env = models.ForeignKey('Profile', models.DO_NOTHING, db_column='profile_env')
    status_signal = models.IntegerField(blank=True, null=True)
    status_video = models.IntegerField(blank=True, null=True)
    status_audio = models.IntegerField(blank=True, null=True)
    is_mnt_signal = models.IntegerField(blank=True, null=True)
    is_mnt_video = models.IntegerField(blank=True, null=True)
    is_mnt_audio = models.IntegerField(blank=True, null=True)
    is_enable = models.IntegerField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'monitor'
        unique_together = (('agent_ip_control', 'profile_channel', 'profile_quality', 'profile_env'),)


class MulticastIp(models.Model):
    ip = models.CharField(primary_key=True, max_length=15)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'multicast_ip'


class ProfileQuality(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    quality = models.CharField(max_length=45)
    description = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'profile_quality'


class SatelliteDisheHasMulticastIp(models.Model):
    satellite_dishe = models.ForeignKey('SatelliteDishe', models.DO_NOTHING, primary_key=True)
    multicast_ip_ip = models.ForeignKey(MulticastIp, models.DO_NOTHING, db_column='multicast_ip_ip')

    class Meta:
        managed = True
        db_table = 'satellite_dishe_has_multicast_ip'
        unique_together = (('satellite_dishe', 'multicast_ip_ip'),)


class User(models.Model):
    username = models.CharField(unique=True, max_length=30, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'


class UserHasMulticastIp(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, primary_key=True)
    multicast_ip = models.ForeignKey(MulticastIp, models.DO_NOTHING, db_column='multicast_ip')
    pou = models.CharField(max_length=60, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user_has_multicast_ip'
        unique_together = (('user', 'multicast_ip'),)


class Vlan(models.Model):
    id = models.IntegerField(primary_key=True)
    env = models.CharField(max_length=30)
    provider = models.ForeignKey('VlanProvider', models.DO_NOTHING, db_column='provider')
    desc = models.CharField(max_length=60, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vlan'
        unique_together = (('id', 'env', 'provider'),)


class VlanProvider(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    address = models.CharField(max_length=60, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vlan_provider'
