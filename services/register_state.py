import json

from services.decorators import r_state, w_state, rw_state

@w_state
def init_register():
    return {
        'state': 0,
        'days': 0,
        'day-profit': 0,
        'day-count': 0
    }


@rw_state
def change_state(data):
    state = data.get('state')

    if state:
        data['days'] += 1
        data['day-count'] = 0
        data['day-profit'] = 0

    data['state'] = int(not state)
    return data

@rw_state
def increase_profit(data, n: int):
    if(data.get('state') == 1):
        data['day-profit'] += n
        data['day-count'] += 1

    return data

@r_state
def get_register_state(data):
    return data.get('state')

@r_state
def get_day_profit(data):
    return -1 if not data.get('state') else data.get('day-profit')
    






