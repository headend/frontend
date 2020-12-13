from django.contrib import admin
from .models import (
					GroupProfile,
					GroupProfileHasProfile,
					Profile,
					ProfileQuality,
					EncoderInputProfile,
					Monitor,
					AgentHasGroupProfile
					)

# Register your models here.

admin.site.register(GroupProfile)
admin.site.register(GroupProfileHasProfile)
admin.site.register(Profile)
admin.site.register(ProfileQuality)
admin.site.register(EncoderInputProfile)
admin.site.register(Monitor)
admin.site.register(AgentHasGroupProfile)