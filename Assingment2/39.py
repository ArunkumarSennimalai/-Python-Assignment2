import datetime
import calendar

def printCurrentDateTime(today):
    formattedDateTime = today.strftime("%d/%m/%Y %H:%M:%S")
    print formattedDateTime

def printCurrentMonthCalendar(today):
    print calendar.month(today.year,today.month)

if __name__ == "__main__":
    try:
       today = datetime.datetime.now()
       printCurrentDateTime(today)
       printCurrentMonthCalendar(today)
    except Exception as e:
        print(e)
        
        
