from menu.base import Menu, Option
from menu.input_menu import input_menu


def change_register_state():
    print('register changed')

type_face = Option(
    'type face',
    None,
    lambda: print(
        '''
        ^-^
        '''
    )
)

type_value = Option(
    'open/close register',
    None,
    lambda: print('value')
)

type_menu = Menu(
    'Start Day',
    [
        type_face,
        type_value,
    ]
)