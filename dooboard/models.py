from django.db import models

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
    ERA=models.FloatField()
    K=models.IntegerField()
    inning=models.FloatField()
    win=models.IntegerField()
    loss=models.IntegerField()
    saves=models.IntegerField()
    hold=models.IntegerField()
   
class BatterDataLS(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    AVG=models.FloatField()
    OBP=models.FloatField()
    SLG=models.FloatField()
    PA=models.IntegerField()
    hit=models.IntegerField()
    homerun=models.IntegerField()
    BOB=models.IntegerField()
class Reply(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()