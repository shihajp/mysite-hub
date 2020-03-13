from django import forms
from .models import Friend,Message

class HelloForm(forms.Form):

    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender',required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']

class FindForm(forms.Form):
    find = forms.CharField(label='Find',required=False)

class CheckForm(forms.Form):
    date = forms.DateField(label='Date',input_formats=['%d'])

    time = forms.TimeField(label='Time')
    datetime = forms.DateTimeField(label='DateTime')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'friend']



