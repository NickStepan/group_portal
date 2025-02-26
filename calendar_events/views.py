from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, datetime
from utils import setup_context
import calendar
from .models import Event
from .forms import EventForm

# Словник для переводу назв місяців українською
MONTHS_UA = {
    1: "Січень", 2: "Лютий", 3: "Березень", 4: "Квітень",
    5: "Травень", 6: "Червень", 7: "Липень", 8: "Серпень",
    9: "Вересень", 10: "Жовтень", 11: "Листопад", 12: "Грудень"
}

# Перенаправлення на поточний місяць
def calendar_redirect(request):
    today = date.today()
    return redirect('calendar_by_month', year=today.year, month=today.month)

# Генерація HTML-календаря з подіями
def calendar_view(request, year, month):
    today = date.today()
    month_days = calendar.monthcalendar(year, month)
    events = Event.objects.filter(date__year=year, date__month=month)
    event_days = events.values_list('date__day', flat=True)

    cal_html = '<table>'
    cal_html += f'<tr><th colspan="7" style="text-align: center; font-size: 18px; font-weight: bold;">{MONTHS_UA[month]} {year}</th></tr>'
    cal_html += '<tr><th>Пн</th><th>Вт</th><th>Ср</th><th>Чт</th><th>Пт</th><th>Сб</th><th>Нд</th></tr>'

    for week in month_days:
        cal_html += '<tr>'
        for day in week:
            if day == 0:
                cal_html += '<td></td>'
            elif day in event_days:
                cal_html += f'<td><a href="/calendar/{year}/{month}/{day}/" style="color: blue; font-weight: bold;">{day}</a></td>'
            else:
                cal_html += f'<td>{day}</td>'
        cal_html += '</tr>'
    cal_html += '</table>'

    form = EventForm()

    return render(request, 'calendar_events/calendar.html', setup_context(request,{
        'calendar': cal_html,
        'year': year,
        'month': month,
        'month_name': MONTHS_UA[month],
        'prev_year': year if month > 1 else year - 1,
        'prev_month': month - 1 if month > 1 else 12,
        'next_year': year if month < 12 else year + 1,
        'next_month': month + 1 if month < 12 else 1,
        'events': events,
        'form': form,
    }))

# Відображення подій конкретного дня
def day_view(request, year, month, day):
    events = Event.objects.filter(date=date(year, month, day))
    return render(request, 'calendar_events/day_view.html',setup_context(request,{
        'events': events,
        'date': f"{day} {MONTHS_UA[month]} {year}"
    }))

# Додавання події
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_by_month', year=form.cleaned_data['date'].year, month=form.cleaned_data['date'].month)
    else:
        form = EventForm()

    return render(request, 'calendar_events/add_event.html', setup_context(request,{'form': form}))
