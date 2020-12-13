from django.contrib import admin
from .models import (
					Agent,
					AgentHasGroupProfile,
					AgentHasVlan,
					Channel,
					Encoder,
					EncoderHasVlan,
					EncoderInputProfile,
					Enviroment,
					GroupChannel,
					GroupChannelHasChannel,
					GroupProfile,
					GroupProfileHasProfile,
					Monitor,
					MulticastIp,
					Profile,
					ProfileQuality,
					SatelliteDishe,
					SatelliteDisheHasMulticastIp,
					UserHasMulticastIp,
					Vlan,
					VlanProvider
					)

# Register your models here.

admin.site.register(Agent)
admin.site.register(AgentHasGroupProfile)
admin.site.register(AgentHasVlan)
admin.site.register(Channel)
admin.site.register(Encoder)
admin.site.register(EncoderHasVlan)
admin.site.register(EncoderInputProfile)
admin.site.register(Enviroment)
admin.site.register(GroupChannel)
admin.site.register(GroupChannelHasChannel)
admin.site.register(GroupProfile)
admin.site.register(GroupProfileHasProfile)
admin.site.register(Monitor)
admin.site.register(MulticastIp)
admin.site.register(Profile)
admin.site.register(ProfileQuality)
admin.site.register(SatelliteDishe)
admin.site.register(SatelliteDisheHasMulticastIp)
admin.site.register(UserHasMulticastIp)
admin.site.register(Vlan)
admin.site.register(VlanProvider)
