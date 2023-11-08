from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Player, BatterData,PitcherData,Reply
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .forms import ReplyForm
from django.contrib.auth.decorators import login_required
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
@login_required(login_url='common:login')
def reply_create(request, player_id):
    player= get_object_or_404(Player, pk=player_id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.create_date = timezone.now()
            reply.player = player
            reply.author=request.user
            reply.save()
            return redirect('doobo:detail',player_id=player.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'player': player, 'form': form}
    return render(request, 'dooboard/detail.html', context)
@login_required(login_url='common:login')
def reply_modify(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    if request.user != reply.author:
        return redirect('doobo:detail', player_id=reply.player.id)
    if request.method == "POST":
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.modify_date = timezone.now()
            reply.save()
            return redirect('doobo:detail', player_id=reply.player.id)
    else:
        form = ReplyForm(instance=reply)
    context = {'reply': reply, 'form': form}
    return render(request, 'dooboard/reply_form.html', context)
@login_required(login_url='common:login')
def reply_delete(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    if request.user != reply.author:
        pass
    else:
        reply.delete()
    return redirect('doobo:detail', player_id=reply.player.id)