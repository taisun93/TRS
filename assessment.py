import datetime
import argparse

def get_weekday_count(startDate, endDate):
    count = 0
    #Could be more optimized if I counted out the weeks and added 5 for each but this is cleaner
    for day in range(int((endDate-startDate).days)+1):
        if (startDate + datetime.timedelta(day)).weekday() < 5:
            count+=1

    return count

def get_leap_year_day(year):
    if year % 4 == 0:
        return 1
    return 0


def main():

    parser = argparse.ArgumentParser()
    #Dates are expected in YYYY-MM-DD format
    parser.add_argument('startDate', type=str)
    parser.add_argument('endDate', type=str)

    args = parser.parse_args()

    start_date = list(map(int, args.startDate.split('-')))
    end_date = list(map(int, args.endDate.split('-')))
    

    # print(get_weekday_count(args.startDate, args.endDate))

if __name__ == "__main__":
    main()