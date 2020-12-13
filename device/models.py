# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from iptvresource.models import IptvEnviroment, MulticastIp, Vlan


class Encoder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    ip = models.CharField(unique=True, max_length=45, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    hardware = models.CharField(max_length=45, blank=True, null=True)
    desc = models.CharField(max_length=45, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    enviroment = models.ForeignKey(IptvEnviroment, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'encoder'
    def __str__(self):
        return u'%s '%(self.name)



class EncoderHasVlan(models.Model):
    id = models.AutoField(primary_key=True)
    vlan = models.ForeignKey(Vlan, models.CASCADE)
    encoder = models.ForeignKey(Encoder, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'encoder_has_vlan'
        unique_together = (('vlan', 'encoder'),)

    def __str__(self):
        return u'%s | vlanid %s'%(self.encoder, self.vlan)


class SatelliteDishe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    diameter = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=60, blank=True, null=True)
    is_enable = models.BooleanField() 
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)
    env = models.ForeignKey(IptvEnviroment, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'satellite_dishe'
        unique_together = (('id', 'env'),)
    def __str__(self):
        return u'%s - enviroment %s'%(self.name, self.env)    


class SatelliteDisheHasMulticastIp(models.Model):
    id = models.AutoField(primary_key=True)
    satellite_dishe = models.ForeignKey(SatelliteDishe, models.CASCADE)
    multicast_ip = models.ForeignKey(MulticastIp, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'satellite_dishe_has_multicast_ip'
        unique_together = (('multicast_ip', 'satellite_dishe'),)
    def __str__(self):
        return u'%s | %s'%(self.satellite_dishe, self.multicast_ip)   


