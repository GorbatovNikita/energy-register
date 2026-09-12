from menu.start_menu.menu import type_menu



command = 0
current_menu = type_menu


while command != -1:

    current_option_list = current_menu.get_option_list()

    print(current_menu.get_title(), end = '\n')
    
    for e in range(len(current_option_list)):
        print(f"{e}: {current_option_list[e].get_title()}")
        

    command = int(input())

    current_option = current_option_list[command]
    current_menu = current_option.get_next_menu() if current_option.get_next_menu() is not None else type_menu

    print(current_option.execute())

    print('-' * 10)




    