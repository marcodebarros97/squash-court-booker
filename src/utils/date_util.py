from datetime import datetime, timedelta, date


def add_one_week_to_date():
    start_date = date.today()
    start_date_str = start_date.strftime('%d-%m-%Y')
    start_date = datetime.strptime(start_date_str, '%d-%m-%Y')
    one_week = datetime.timedelta(weeks=1)
    end_date = start_date + one_week
    end_date_str = end_date.strftime('%d-%m-%Y')
    print(end_date_str)
