import calendar
import datetime

import PySimpleGUI as sg


sg.theme('LightGray')
weekday = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
today = datetime.date.today()
calen = calendar.Calendar(firstweekday=6)
days = calen.monthdatescalendar(today.year, today.month)

layout = [[sg.Text(today.year, font=(None, 13, 'bold'))],
          [sg.Push(), sg.Button('<'), sg.Text(today.month, font=(None, 30)), sg.Button('>'), sg.Push()]]
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

window = sg.Window('Simple Calendar', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
