from phases_and_constants.other_constants import SEPARATOR
import phases_and_constants.phase_constants as phase_const
import phases_and_constants.subphases_constants as subphases_const
from time import sleep


def weight_conversion_menu():
    sleep(1)
    print("\n\n\tWEIGHT CONVERSION MENU\n" + SEPARATOR + "\nYou have chosen to convert units of weight. But first, choose what you want to convert to what.\n" + SEPARATOR)
    menu_units_of_weight_list = ["Go back to main menu", "Ounce(oz) to Gram(g) conversion", "Gram(g) to Ounce(oz) conversion", "Pound(lb) to Kilogram(kg) conversion", "Kilogram(kg) to Pound(lb) conversion", "Pound(lb) to Ounce(oz) conversion", "Ounce (oz) to Pound(lb) conversion", "Kilogram(kg) to Gram(g) conversion", "Gram(g) to Kilogram(kg) conversion", "Metric Ton(t) to Kilogram(kg) conversion", "Kilogram(kg) to Metric Ton(t) conversion",]
    
    enumerate_menu_units_of_weight_dict = dict(enumerate(menu_units_of_weight_list))
    for k, v in enumerate_menu_units_of_weight_dict.items():
        print(k, " - ", v)
    print("")
    
    while True:
        user_input = input("Your choice is: ")
        if user_input == "0":
            sleep(1)
            return phase_const.MAIN_MENU_PHASE
        elif user_input == "1":
            sleep(1)
            return subphases_const.OUNCE_TO_GRAM
        elif user_input == "2":
            sleep(1)
            return subphases_const.GRAM_TO_OUNCE
        elif user_input == "3":
            sleep(1)
            return subphases_const.POUND_TO_KILOGRAM
        elif user_input == "4":
            sleep(1)
            return subphases_const.KILOGRAM_TO_POUND
        elif user_input == "5":
            sleep(1)
            return subphases_const.POUND_TO_OUNCE
        elif user_input == "6":
            sleep(1)
            return subphases_const.OUNCE_TO_POUND
        elif user_input == "7":
            sleep(1)
            return subphases_const.KILOGRAM_TO_GRAM
        elif user_input == "8":
            sleep(1)
            return subphases_const.GRAM_TO_KILOGRAM
        elif user_input == "9":
            sleep(1)
            return subphases_const.METRIC_TON_TO_KILOGRAM
        elif user_input == "10":
            sleep(1)
            return subphases_const.KILOGRAM_TO_METRIC_TON
        else:
            print("Out of range.")
            continue
