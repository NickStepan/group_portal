from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from utils import setup_context
import calendar
from .models import Event
from .forms import EventForm

MONTHS_UA_NOM = {
    1: "Січень", 2: "Лютий", 3: "Березень", 4: "Квітень",
    5: "Травень", 6: "Червень", 7: "Липень", 8: "Серпень",
    9: "Вересень", 10: "Жовтень", 11: "Листопад", 12: "Грудень"
}

MONTHS_UA_GEN = {
    1: "січня", 2: "лютого", 3: "березня", 4: "квітня",
    5: "травня", 6: "червня", 7: "липня", 8: "серпня",
    9: "вересня", 10: "жовтня", 11: "листопада", 12: "грудня"
}

def calendar_redirect(request):
    today = date.today()
    return redirect('calendar_by_month', year=today.year, month=today.month)

def calendar_view(request, year, month):
    today = date.today()
    month_days = calendar.monthcalendar(year, month)
    events = Event.objects.filter(date__year=year, date__month=month)
    completed_events = events.filter(completed=True)
    uncompleted_events = events.filter(completed=False)
    event_days = events.values_list('date__day', flat=True)
    completed_event_days = completed_events.values_list('date__day', flat=True)

    cal_html = '<table>'
    cal_html += f'<tr><th colspan="7" style="text-align: center; font-size: 18px; font-weight: bold;">{MONTHS_UA_NOM[month]} {year}</th></tr>'
    cal_html += '<tr><th>Пн</th><th>Вт</th><th>Ср</th><th>Чт</th><th>Пт</th><th>Сб</th><th>Нд</th></tr>'

    for week in month_days:
        cal_html += '<tr>'
        for day in week:
            if day == 0:
                cal_html += '<td></td>'
            elif day in completed_event_days:
                cal_html += f'<td class="event-day completed-event" style="color: purple; font-weight: bold;">{day}</td>'
            elif day in event_days:
                cal_html += f'<td class="event-day">{day}</td>'
            else:
                cal_html += f'<td>{day}</td>'
        cal_html += '</tr>'
    cal_html += '</table>'

    form = EventForm()

    return render(request, 'calendar_events/calendar.html', setup_context(request, {
        'calendar': cal_html,
        'year': year,
        'month': month,
        'month_name_nom': MONTHS_UA_NOM[month],  # Називний відмінок для заголовка
        'month_name_gen': MONTHS_UA_GEN[month],  # Родовий відмінок для подій
        'prev_year': year if month > 1 else year - 1,
        'prev_month': month - 1 if month > 1 else 12,
        'next_year': year if month < 12 else year + 1,
        'next_month': month + 1 if month < 12 else 1,
        'events': uncompleted_events,
        'completed_events': completed_events,
        'form': form,
    }))

def day_view(request, year, month, day):
    events = Event.objects.filter(date=date(year, month, day))
    return render(request, 'calendar_events/day_view.html', setup_context(request, {
        'events': events,
        'date': f"{day} {MONTHS_UA_GEN[month]} {year}"  # Використання родового відмінка
    }))

def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_by_month', year=form.cleaned_data['date'].year, month=form.cleaned_data['date'].month)
    else:
        form = EventForm()

    return render(request, 'calendar_events/add_event.html', setup_context(request, {'form': form}))

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        event.delete()
        return redirect('calendar_by_month', year=event.date.year, month=event.date.month)

    return render(request, 'calendar_events/confirm_delete.html', setup_context(request, {'event': event}))

def mark_completed(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.completed = not event.completed
    event.save()
    return redirect('calendar_by_month', year=event.date.year, month=event.date.month)
