from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Player, BatterData,PitcherData
from django.utils import timezone
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
def reply_create(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    player.reply_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('doobo:detail',player_id=player.id)