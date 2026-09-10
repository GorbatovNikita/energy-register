from menu.base import Menu, Option


def print_value():
    print(input('Input printable'))


print_input = Option(
    'print input',
    None,
    print_value,

)

input_menu = Menu(
    'input menu',
    [
        print_input,
    ]
)