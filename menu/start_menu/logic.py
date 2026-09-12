from services.register_state import change_state, init_register, increase_profit, get_register_state, get_day_profit
from menu.base import option_input_int, option_input_str


def change_register_state():
    change_state()
    return 'Success'

@option_input_str('You sure you want to refresh current register state?(it will NOT delete sales,\nbut initialize/reinitialize current fast access state data)(y/n): ')
def refresh_register(value: str):
    if value == "y":
        init_register()
    return 'Success'


@option_input_int('Enter sale size')
def make_sale(value: int):
    increase_profit(value)
    return 'Success'

def get_state():
    return 'opened' if get_register_state() else 'closed'

def get_profit():
    profit = get_day_profit()
    return f'{profit} ₽' if profit != -1 else 'register is closed'
    