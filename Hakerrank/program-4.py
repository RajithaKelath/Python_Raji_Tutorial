import calendar

weekDays = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

if __name__ == '__main__':
    month, day, year = map(int, input().split())
    #print(weekDays[calendar.weekday(year, month, day)].upper())
    print((calendar.day_name[calendar.weekday(year, month, day)]).upper())