from django.contrib import admin
from .models import (
					Encoder,
					EncoderHasVlan,
					SatelliteDishe,
					SatelliteDisheHasMulticastIp
					)

# Register your models here.

admin.site.register(Encoder)
admin.site.register(EncoderHasVlan)
admin.site.register(SatelliteDishe)
admin.site.register(SatelliteDisheHasMulticastIp)