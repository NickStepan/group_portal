from django.shortcuts import render
import calendar
from datetime import datetime, timedelta

def calendar_view(request, year=None, month=None):
    if year is None or month is None:
        now = datetime.now()
        year, month = now.year, now.month

    # Переконуємося, що рік і місяць - це числа
    year, month = int(year), int(month)

    # Генеруємо календар
    cal = calendar.HTMLCalendar().formatmonth(year, month)

    # Визначаємо попередній і наступний місяць
    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1

    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    return render(request, 'calendar_events/calendar.html', {
        'calendar': cal,
        'year': year,
        'month': month,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month
    })
