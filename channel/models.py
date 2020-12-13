# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)
    date_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'channel'


class GroupChannel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30, blank=True, null=True)
    desc = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'group_channel'


class GroupChannelHasChannel(models.Model):
    id = models.AutoField(primary_key=True)
    group_channel = models.ForeignKey(GroupChannel, models.CASCADE)
    channel = models.ForeignKey(Channel, models.CASCADE)

    class Meta:
        managed = True
        db_table = 'group_channel_has_channel'
        unique_together = (('channel', 'group_channel'),)
