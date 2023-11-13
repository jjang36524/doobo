from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Player(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=20)
    position=models.CharField(max_length=20)
    birth=models.DateField(max_length=20)
    enter=models.IntegerField()
    pay=models.IntegerField()
    handtype=models.CharField(max_length=20)
    ispitcher=models.BooleanField()
    games=models.IntegerField()
    curgames=models.IntegerField()
    image=models.CharField(max_length=200,null=True)
    voteru = models.ManyToManyField(User,related_name='voteru_question')
    voterd = models.ManyToManyField(User,related_name='voterd_question')
    def altpay(self):
        return self.pay/10000
class PitcherData(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    ERA=models.FloatField()
    K=models.IntegerField()
    inning=models.FloatField()
    win=models.IntegerField()
    loss=models.IntegerField()
    saves=models.IntegerField()
    hold=models.IntegerField()
   
class BatterData(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    AVG=models.FloatField()
    OBP=models.FloatField()
    SLG=models.FloatField()
    PA=models.IntegerField()
    hit=models.IntegerField()
    homerun=models.IntegerField()
    BOB=models.IntegerField()
class PitcherDataLS(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    ERAl=models.FloatField()
    Kl=models.IntegerField()
    inningl=models.FloatField()
    winl=models.IntegerField()
    lossl=models.IntegerField()
    savesl=models.IntegerField()
    holdl=models.IntegerField()
   
class BatterDataLS(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    AVGl=models.FloatField()
    OBPl=models.FloatField()
    SLGl=models.FloatField()
    PAl=models.IntegerField()
    hitl=models.IntegerField()
    homerunl=models.IntegerField()
    BOBl=models.IntegerField()
class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author_reply')
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date=models.DateTimeField(null=True)
    voteru = models.ManyToManyField(User,related_name='voteru_reply')
    voterd = models.ManyToManyField(User,related_name='voterd_reply')
class Verified(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)