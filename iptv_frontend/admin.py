from django.contrib import admin
from .models import Agent
        """
        Channel,
        Encoder,
        Env,
        MulticastIp,
        Vlan,
        Profile)
"""

# Register your models here.
admin.site.register(Agent)
"""
admin.site.register(Channel)
admin.site.register(Encoder)
admin.site.register(MulticastIp)
admin.site.register(Vlan)
admin.site.register(Profile)
"""
