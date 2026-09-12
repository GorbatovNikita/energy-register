from menu.base import Menu, Option
from menu.start_menu.logic import refresh_register, change_register_state, make_sale, get_state, get_profit





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
    'Main menu',
    [
        refresh_register_option,
        get_register_state_option,
        get_day_profit_option,
        make_sale_option,
        open_register_option,

        
    ]
)