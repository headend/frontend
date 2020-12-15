from django.contrib import admin
from .models import (
					Channel,
					GroupChannel,
					GroupChannelHasChannel,					)

# Register your models here.

admin.site.register(Channel)
admin.site.register(GroupChannel)
admin.site.register(GroupChannelHasChannel)

