from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, BatterData,PitcherData
def index(request):
    player_list = Player.objects.order_by('no')
    batterdata = BatterData.objects.order_by('player')
    pitcherdata = PitcherData.objects.order_by('player')

    context = {'player_list': player_list,'batterdata':batterdata,'pitcherdata':pitcherdata}
    return render(request, 'dooboard/index.html', context)
def detail(request, player_id):
    player = Player.objects.get(id=player_id)
    context = {'player': player}
    return render(request, 'dooboard/detail.html', context)