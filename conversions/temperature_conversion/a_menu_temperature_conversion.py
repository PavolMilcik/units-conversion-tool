from phases_and_constants.other_constants import SEPARATOR
import phases_and_constants.phase_constants as phase_const
import phases_and_constants.subphases_constants as subphases_const
from time import sleep


def temperature_conversion_menu():
    sleep(1)
    print("\n\n\tTEMPERATURE CONVERSION MENU\n" + SEPARATOR + "\nYou have chosen to convert temperature. But first, choose what you want to convert to what.\n" + SEPARATOR)
    menu_temperature_list = ["Go back to main menu", "Fahrenheit(°F) to Celsius(°C) conversion", "Celsius(°C) to Farhenheit(°F) conversion"]
    
    enumerate_menu_temperature_dict = dict(enumerate(menu_temperature_list))
    for k, v in enumerate_menu_temperature_dict.items():
        print(k, " - ", v)
    print("")
    
    while True:
        user_input = input("Your choice is: ")
        if user_input == "0":
            sleep(1)
            return phase_const.MAIN_MENU_PHASE
        elif user_input == "1":
            sleep(1)
            return subphases_const.FAHRENHEIT_TO_CELSIUS
        elif user_input == "2":
            sleep(1)
            return subphases_const.CELSIUS_TO_FAHRENHEIT
        else:
            print("Out of range.")
            continue
