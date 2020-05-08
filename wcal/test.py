
import calendar

# Создаем обычный текстовый календарь
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(2020, 5, 0, 0)
print(str)

# Создаем календарь в формате HTML
hc = calendar.HTMLCalendar(calendar.MONDAY)
str = hc.formatmonth(2020, 5)
print(str)
# перебираем через цикл дни месяца
# нули указывают, что дни принадлежат смежному месяцу
