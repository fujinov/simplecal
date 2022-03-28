import calendar
import datetime


weekday = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
today = datetime.date.today()
calen = calendar.Calendar(firstweekday=6)
days = calen.monthdatescalendar(today.year, today.month)
