import datetime
import argparse

def get_weekday_count(startDate, endDate):
    count = 0
    #Could be more optimized if I counted out the weeks and added 5 for each but this is cleaner
    for day in range(int((endDate-startDate).days)+1):
        if (startDate + datetime.timedelta(day)).weekday() < 5:
            count+=1

    return count

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('startDate', type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date())
    parser.add_argument('endDate', type=lambda d: datetime.datetime.strptime(d, '%Y-%m-%d').date())

    args = parser.parse_args()

    print(get_weekday_count(args.startDate, args.endDate))

if __name__ == "__main__":
    main()