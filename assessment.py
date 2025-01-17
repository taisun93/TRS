import argparse


def get_weekday_count(startDay, endDay):
    duration = endDay - startDay + 1

    whole_weeks = duration // 7

    remainder = duration % 7 

    weekday_count = 0
    # Count the weekdays in the remainder days
    for day in range(remainder):
        if day_of_week(startDay + day) < 5:  
            weekday_count += 1

    return whole_weeks * 5 + weekday_count


def get_total_day(year, month, day):

    completed_year = year-1

    leap_year_count = (completed_year // 4) - (completed_year // 100) + (completed_year // 400)

    year_day_count = 365 * completed_year + leap_year_count

    month_list = [
        31,
        28 + get_leap_year_day(year),
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31,
    ]

    month_day_count = sum(month_list[:month - 1])

    return year_day_count + month_day_count + day


def get_leap_year_day(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            return 0
        return 1
    return 0


def day_of_week(total_days):
    # January 1, 1 CE was a saturday
    return (total_days + 6) % 7


def main():

    parser = argparse.ArgumentParser()
    # Dates are expected in YYYY-MM-DD format
    parser.add_argument("startDate", type=str)
    parser.add_argument("endDate", type=str)

    args = parser.parse_args()

    start_date = list(map(int, args.startDate.split("-")))
    end_date = list(map(int, args.endDate.split("-")))

    print(get_weekday_count(get_total_day(*start_date), get_total_day(*end_date)))


if __name__ == "__main__":
    main()
