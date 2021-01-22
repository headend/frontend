# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class MonitorLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    agent_id = models.BigIntegerField(blank=True, null=True)
    profile_id = models.BigIntegerField(blank=True, null=True)
    monitor_id = models.BigIntegerField(blank=True, null=True)
    channel_id = models.BigIntegerField(blank=True, null=True)
    channel_name = models.CharField(max_length=255, blank=True, null=True)
    multicast_ip = models.CharField(max_length=255, blank=True, null=True)
    before_status = models.BigIntegerField(blank=True, null=True)
    before_signal_status = models.IntegerField(blank=True, null=True)
    before_video_status = models.IntegerField(blank=True, null=True)
    before_audio_status = models.IntegerField(blank=True, null=True)
    after_status = models.BigIntegerField(blank=True, null=True)
    after_signal_status = models.IntegerField(blank=True, null=True)
    after_video_status = models.IntegerField(blank=True, null=True)
    after_audio_status = models.IntegerField(blank=True, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    date_create = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'monitor_logs'

