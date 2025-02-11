from django.shortcuts import render
import calendar
from datetime import datetime

def calendar_view(request):
    year = datetime.now().year
    month = datetime.now().month
    cal = calendar.HTMLCalendar().formatmonth(year, month)
    
    return render(request, 'calendar_events/calendar.html', {'calendar': cal, 'year': year, 'month': month})
