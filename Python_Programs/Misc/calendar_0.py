import calendar
y = int(input("Enter year: "))
print(f"Is year leap?: {calendar.isleap(y)}")
t = calendar.TextCalendar()
print(f"Printing March {y} calendar:")
print(t.formatmonth(theyear=y, themonth=3))
cal = calendar.Calendar()
print(f"Printing month dates for March {y}:")
im = cal.itermonthdates(year=y, month=3)
for i in im:
    print(i)
print(f"Printing month days for April {y}:")
ca = calendar.Calendar()
cm = ca.monthdayscalendar(year=y, month=4)
for i in cm:
    print(i)
print(f"Printing calender for year: {y}")
print(calendar.calendar(y))

cb = calendar.LocaleHTMLCalendar()
print(cb.monthdayscalendar(year=2022, month=11))

