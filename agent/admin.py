from django.contrib import admin
from .models import (
					Agent,
					AgentHasVlan,
					)

# Register your models here.

admin.site.register(Agent)
admin.site.register(AgentHasVlan)
