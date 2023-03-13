import datetime
import logging
from datetime import datetime, timedelta


def determine_second_slot(first_slot: str):
    try:
        start_time = datetime.strptime(first_slot, '%H:%M')
        second_slot = start_time + timedelta(minutes=30)
        return second_slot.strftime('%H:%M')
    except ValueError:
        print('Correct Page Retrieved, Performing Login')
        logging.info('Correct Page Retrieved, Performing Login')
