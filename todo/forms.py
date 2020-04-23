from django import forms
from .models import Todo
from accounts.models import User


class TodoForm(forms.ModelForm):
    title = forms.CharField()
    done = forms.BooleanField()
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.HiddenInput()
    )
    title.widget.attrs.update({'class': 'input'})
    done.widget.attrs.update({'class': 'input'})

    class Meta:
        model = Todo
        fields = ['title', 'done', 'user']
