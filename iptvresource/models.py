# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from  django.contrib.auth.models import User as AuthUser


class VlanProvider(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    address = models.CharField(max_length=60, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'vlan_provider'
    def __str__(self):
        return self.name

class IptvEnviroment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    desc = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'enviroment'
    def __str__(self):
        return self.name

class MulticastIp(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(unique=True, max_length=15, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'multicast_ip'
    def __str__(self):
        return self.ip


class UserHasMulticastIp(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.CASCADE)
    multicast_ip = models.ForeignKey(MulticastIp, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'user_has_multicast_ip'
        unique_together = (('multicast_ip', 'user'),)
    def __str__(self):
        return u'User %s has ip: %s'%(self.user.username, self.multicast_ip)


class Vlan(models.Model):
    id = models.AutoField(primary_key=True)
    vlanid = models.CharField(max_length=30)
    desc = models.CharField(max_length=60, blank=True, null=True)
    is_enable = models.BooleanField() 
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    env = models.ForeignKey(IptvEnviroment, models.CASCADE)
    vlan_provider = models.ForeignKey(VlanProvider, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'vlan'
        unique_together = (('vlan_provider', 'env', 'vlanid'),)
    def __str__(self):
        return u'Vlanid %s - %s - %s'%(self.vlanid, self.env, self.vlan_provider)
