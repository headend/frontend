# Generated by Django 2.2.12 on 2020-12-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_agent_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='audio_monitor',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='date_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='is_alarm',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='is_monitor',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='run_thread',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='signal_monitor',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='video_monitor',
            field=models.BooleanField(default=False, null=True),
        ),
    ]