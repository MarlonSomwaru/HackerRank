import calendar

month, day, year=input().split(" ")

month=int(month)
day=int(day)
year=int(year)

weekNum=calendar.weekday(year, month, day)
dayList=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

print(dayList[weekNum])