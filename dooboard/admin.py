from django.contrib import admin

# Register your models here.
from .models import Player,PitcherData,BatterData

admin.site.register(Player)
admin.site.register(PitcherData)
admin.site.register(BatterData)