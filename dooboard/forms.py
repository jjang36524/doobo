from django import forms
from dooboard.models import Reply
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': '답변내용',
        }