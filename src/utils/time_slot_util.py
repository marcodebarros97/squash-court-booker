import datetime
import logging
from datetime import datetime, timedelta


def add_one_hour_to_time(first_slot: str):
    try:
        start_time = datetime.strptime(first_slot, '%H:%M')
        second_slot = start_time + timedelta(hours=1)
        return second_slot.strftime('%H:%M')
    except ValueError:
        print('Correct Page Retrieved, Performing Login')
        logging.info('Correct Page Retrieved, Performing Login')