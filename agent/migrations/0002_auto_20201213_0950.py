# Generated by Django 2.2.12 on 2020-12-13 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenthasgroupprofile',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Agent'),
        ),
        migrations.AlterField(
            model_name='agenthasgroupprofile',
            name='group_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.GroupProfile'),
        ),
        migrations.AlterField(
            model_name='agenthasvlan',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Agent'),
        ),
        migrations.AlterField(
            model_name='agenthasvlan',
            name='vlan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Vlan'),
        ),
        migrations.AlterField(
            model_name='encoder',
            name='enviroment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Enviroment'),
        ),
        migrations.AlterField(
            model_name='encoderhasvlan',
            name='encoder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Encoder'),
        ),
        migrations.AlterField(
            model_name='encoderhasvlan',
            name='vlan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Vlan'),
        ),
        migrations.AlterField(
            model_name='encoderinputprofile',
            name='encoder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Encoder'),
        ),
        migrations.AlterField(
            model_name='encoderinputprofile',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Profile'),
        ),
        migrations.AlterField(
            model_name='groupchannelhaschannel',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Channel'),
        ),
        migrations.AlterField(
            model_name='groupchannelhaschannel',
            name='group_channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.GroupChannel'),
        ),
        migrations.AlterField(
            model_name='groupprofilehasprofile',
            name='group_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.GroupProfile'),
        ),
        migrations.AlterField(
            model_name='groupprofilehasprofile',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Profile'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Agent'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Channel'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='encoder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Encoder'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='multicast_ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.MulticastIp'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.ProfileQuality'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vlan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Vlan'),
        ),
        migrations.AlterField(
            model_name='satellitedishe',
            name='env',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Enviroment'),
        ),
        migrations.AlterField(
            model_name='satellitedishehasmulticastip',
            name='multicast_ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.MulticastIp'),
        ),
        migrations.AlterField(
            model_name='satellitedishehasmulticastip',
            name='satellite_dishe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.SatelliteDishe'),
        ),
        migrations.AlterField(
            model_name='userhasmulticastip',
            name='multicast_ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.MulticastIp'),
        ),
        migrations.AlterField(
            model_name='userhasmulticastip',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vlan',
            name='env',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Enviroment'),
        ),
        migrations.AlterField(
            model_name='vlan',
            name='vlan_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.VlanProvider'),
        ),
    ]