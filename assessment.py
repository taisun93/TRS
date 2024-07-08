import datetime
import argparse

def get_total_day(year, month, day):

    leap_year_count = (year//4) - (year//100) + (year//400)

    year_day_count = 365 * year +leap_year_count

    month_list = [31, 28 + get_leap_year_day(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month_day_count = 0
    
    for m in range(month):
        month_day_count+=month_list[m]
        
    return year_day_count + month_day_count + day

def day_of_week(total_days):
    # January 1, 1 CE was a Monday (0)
    return (total_days - 1) % 7

def get_leap_year_day(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            return 0
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