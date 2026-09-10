from menu.base import Menu, Option
from menu.input_menu import input_menu
from services.register_state import change_state, init_register, increase_profit, get_register_state, get_day_profit


def change_register_state():
    change_state()

def refresh_register():
    if input('You sure you want to refresh current register state?(it will NOT delete sales,\nbut initialize/reinitialize current fast access state data)(y/n): ').lower() == "y":
        init_register()

def make_sale():
    increase_profit(int(input('Enter sale size: ')))

def get_state():
    print('opened' if get_register_state() else 'closed')

def get_profit():
    profit = get_day_profit()
    print(f'{profit}₽' if profit != -1 else 'register is closed')
    pass




refresh_register_option = Option(
    'Reinialize current register state(firt launch require)',
    None,
    refresh_register,
)
open_register_option = Option(
    'Open/close register',
    None,
    change_register_state,
)
make_sale_option = Option(
    'Add sale to register',
    None,
    make_sale
)

get_register_state_option = Option(
    'Get register state',
    None,
    get_state,
)

get_day_profit_option = Option(
    'Get current profit',
    None,
    get_profit
)


type_menu = Menu(
    'Start Day',
    [
        refresh_register_option,
        get_register_state_option,
        get_day_profit_option,
        make_sale_option,
        open_register_option,

        
    ]
)