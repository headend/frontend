from django.contrib import admin
from .models import (
					VlanProvider,
					IptvEnviroment,
					MulticastIp,
					UserHasMulticastIp,
					Vlan
					)

# Register your models here.

admin.site.register(VlanProvider)
admin.site.register(IptvEnviroment)
admin.site.register(MulticastIp)
admin.site.register(UserHasMulticastIp)
admin.site.register(Vlan)
