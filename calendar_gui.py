import calendar
import datetime

import PySimpleGUI as sg


sg.theme('LightGray1')
weekday = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']  
today = datetime.date.today()
date = today

def create_calendar():
    calen = calendar.Calendar(firstweekday=6)
    days = calen.monthdatescalendar(date.year, date.month)
    layout = [[sg.Text(date.year, font=(None, 13, 'bold'))],
              [sg.Push(), sg.Button('<'), sg.Text(date.month, font=(None, 30)), sg.Button('>'), sg.Push()]]
    inner = []
    for week in weekday:
        inner.append(sg.Text(week, size=(4,1), text_color='white', background_color='green', justification='center'))
    layout.append(inner.copy())

    for row in days:
        inner = []
        for i, day in enumerate(row):
            if today == day:            
                inner.append(sg.Text(day.day, size=(4,1), justification='right', text_color='white', background_color='gray'))
            elif i == 0:
                inner.append(sg.Text(day.day, size=(4,1), justification='right', text_color='red'))
            elif i == 6:
                inner.append(sg.Text(day.day, size=(4,1), justification='right', text_color='blue'))
            else:
                inner.append(sg.Text(day.day, size=(4,1), justification='right'))
        layout.append(inner.copy())
    return layout

layout = create_calendar()
window = sg.Window('Simple Calendar', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '<':
        window.close()
        date = datetime.date(date.year, date.month, 1) - datetime.timedelta(days=1)
        window = sg.Window('Simple Calendar', create_calendar())
    elif event == '>':
        window.close()
        date = datetime.date(date.year, date.month, 28) + datetime.timedelta(days=4)
        window = sg.Window('Simple Calendar', create_calendar())
window.close()
