from django import forms
from dooboard.models import Reply,Player,PitcherData,BatterData,PitcherDataLS,BatterDataLS
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': '답변내용',
        }
class PitcherForm(forms.ModelForm):
    class Meta:
        model=Player
        fields=['no','name','position','birth','enter','pay','handtype','games','curgames','image']
        labels={
            'no':'등번호',
            'name':'이름',
            'position':'포지션',
            'birth':'생일',
            'enter':'입단연도',
            'pay':'연봉',
            'handtype':'쓰는 손',
            'games':'경기 수',
            'curgames':'경기 수(이번 시즌)',
            'image':'이미지 링크',
        }
class PitcherDataForm(forms.ModelForm):
    class Meta:
        model=PitcherData
        fields=['ERA','K','inning','win','loss','saves','hold']
        labels={
            'ERA':'평균자책점',
            'K':'삼진',
            'inning':'이닝',
            'win':'승리',
            'loss':'패배',
            'saves':'세이브',
            'hold':'홀드'
        }
class PitcherLSForm(forms.ModelForm):
    class Meta:
        model=PitcherDataLS
        fields=['ERAl','Kl','inningl','winl','lossl','savesl','holdl']
        labels={
            'ERAl':'평균자책점(이번 시즌)',
            'Kl':'삼진(이번 시즌)',
            'inningl':'이닝(이번 시즌)',
            'winl':'승리(이번 시즌)',
            'lossl':'패배(이번 시즌)',
            'savesl':'세이브(이번 시즌)',
            'holdl':'홀드(이번 시즌)'
        }
class BatterForm(forms.ModelForm):
    class Meta:
        model=Player
        fields=['no','name','position','birth','enter','pay','handtype','games','curgames','image']
        labels={
            'no':'등번호',
            'name':'이름',
            'position':'포지션',
            'birth':'생일',
            'enter':'입단연도',
            'pay':'연봉',
            'handtype':'쓰는 손',
            'games':'경기 수',
            'curgames':'경기 수(이번 시즌)',
            'image':'이미지 링크',
        }
class BatterDataForm(forms.ModelForm):
    class Meta:
        model=BatterData
        fields=['AVG','OBP','SLG','PA','hit','homerun','BOB']
        labels={
           'AVG':'타율','OBP':'출루율','SLG':'장타율','PA':'타석','hit':'안타','homerun':'홈런','BOB':'볼넷'
        }
class BatterLSForm(forms.ModelForm):
    class Meta:
        model=BatterDataLS
        fields=['AVGl','OBPl','SLGl','PAl','hitl','homerunl','BOBl']
        labels={
           'AVGl':'타율(이번 시즌)','OBPl':'출루율(이번 시즌)','SLGl':'장타율(이번 시즌)','PAl':'타석(이번 시즌)','hitl':'안타(이번 시즌)','homerunl':'홈런(이번 시즌)','BOBl':'볼넷(이번 시즌)'
        }