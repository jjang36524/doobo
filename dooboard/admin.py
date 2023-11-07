from django.contrib import admin

# Register your models here.
from .models import Player,PitcherData,BatterData,PitcherDataLS,BatterDataLS

admin.site.register(Player)
admin.site.register(PitcherData)
admin.site.register(BatterData)
admin.site.register(PitcherDataLS)
admin.site.register(BatterDataLS)