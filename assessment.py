import datetime

def get_weekday_count(startDate, endDate):
    count = 0

    for day in range(int((endDate-startDate).days)+1):
        if (startDate + datetime.timedelta(day)).weekday() <= 5:
            count+=1

    return count