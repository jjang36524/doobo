from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from .models import Player, BatterData,PitcherData,Reply
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .forms import ReplyForm,PitcherForm,PitcherDataForm,PitcherLSForm,BatterForm,BatterDataForm,BatterLSForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator  
from django.db.models import Count
def index(request):
    sorts=request.GET.get('sort','1')
    player_list = Player.objects
    print(type(sorts))
    if sorts=='1':
        player_list=player_list.order_by("no")
    elif sorts=='2':
        print(sorts)
        player_list=player_list.annotate(voteu_count=Count('voteru')).order_by('-voteu_count','no')
    elif sorts=='3':
        player_list=player_list.annotate(voted_count=Count('voterd')).order_by('-voted_count','no')
    elif sorts=='4':
        player_list=player_list.annotate(reply_count=Count('reply')).order_by('-reply_count','no')
    else:
        player_list=player_list.order_by("no")
    batterdata = BatterData.objects.order_by('player')
    pitcherdata = PitcherData.objects.order_by('player')
    context = {'player_list': player_list,'batterdata':batterdata,'pitcherdata':pitcherdata}
    return render(request, 'dooboard/index.html', context)
def detail(request, player_id):
    page=request.GET.get('page','1')
    player = Player.objects.get(id=player_id)
    replies=player.reply_set.all().order_by('-create_date')
    paginator = Paginator(replies, 10,allow_empty_first_page=True)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'reply': page_obj,'player': player}
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
@login_required(login_url='common:login')
def player_voteu(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    v=player.voteru.all()
    isin=0
    for i in v:
        if i.id==request.user.id:
            isin=1
    if isin:
        player.voteru.remove(request.user)
    else:
        player.voteru.add(request.user)
    return redirect('doobo:detail', player_id=player.id)
@login_required(login_url='common:login')
def player_voted(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    v=player.voterd.all()
    isin=0
    for i in v:
        if i.id==request.user.id:
            isin=1
    if isin:
        player.voterd.remove(request.user)
    else:
        player.voterd.add(request.user)
    return redirect('doobo:detail', player_id=player.id)
@login_required(login_url='common:login')
def reply_voteu(request, reply_id):
    reply= get_object_or_404(Reply, pk=reply_id)
    v=reply.voteru.all()
    isin=0
    for i in v:
        if i.id==request.user.id:
            isin=1
    if isin:
        reply.voteru.remove(request.user)
    else:
        reply.voteru.add(request.user)
    return redirect('doobo:detail', player_id=reply.player.id)
@login_required(login_url='common:login')
def reply_voted(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    v=reply.voterd.all()
    isin=0
    for i in v:
        if i.id==request.user.id:
            isin=1
    if isin:
        reply.voterd.remove(request.user)
    else:
        reply.voterd.add(request.user)
    return redirect('doobo:detail', player_id=reply.player.id)
def pitcher_add(request):
    if request.method == 'POST':
        form = PitcherForm(request.POST)
        form2 = PitcherDataForm(request.POST)
        form3 = PitcherLSForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.ispitcher=True
            player.save()
            pitcherdata=form2.save(commit=False)
            pitcherdata.player=player
            pitcherdata.save()
            pitcherdatals=form3.save(commit=False)
            pitcherdatals.player=player
            pitcherdatals.save()
            return redirect('doobo:index')
    else:
        form = PitcherForm()
        form2 = PitcherDataForm()
        form3 = PitcherLSForm()
    context = {'form': form,'form2':form2,'form3':form3}
    return render(request, 'dooboard/pitcher_form.html', context)
def batter_add(request):
    if request.method == 'POST':
        form = BatterForm(request.POST)
        form2 = BatterDataForm(request.POST)
        form3 = BatterLSForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.ispitcher=False
            player.save()
            batterdata=form2.save(commit=False)
            batterdata.player=player
            batterdata.save()
            batterdatals=form3.save(commit=False)
            batterdatals.player=player
            batterdatals.save()
            return redirect('doobo:index')
    else:
        form = BatterForm()
        form2 = BatterDataForm()
        form3 = BatterLSForm()
    context = {'form': form,'form2':form2,'form3':form3}
    return render(request, 'dooboard/batter_form.html', context)