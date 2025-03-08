from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date']
        labels = {
            'title': 'Назва події:',
            'description': 'Опис:',
            'date': 'Дата проведення:'
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})  # Віджет вибору дати
        }
