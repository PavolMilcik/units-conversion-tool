from phases_and_constants.other_constants import SEPARATOR
import phases_and_constants.phase_constants as phase_const
import phases_and_constants.subphases_constants as subphases_const
from time import sleep


def dimension_conversion_menu():
    sleep(1)
    print("\n\n\tDIMENSION CONVERSION MENU\n" + SEPARATOR + "\nYou have chosen to convert units of dimension. But first, choose what you want to convert to what.\n" + SEPARATOR)
    menu_units_of_dimension_list = ["Go back to main menu", "Meters(m) to Feet(ft) conversion", "Feet(ft) to Meters(m) conversion", "Meters(m) to Inches(in) conversion", "Inches(in) to Meters(m) conversion", "Centimeters(cm) to Inches(in) conversion", "Inches(in) to Centimeters(cm) conversion", "Kilometers(km) to Miles(mi) conversion", "Miles(mi) to Kilometers(km) conversion", "Meters(m) to Yards(yd) conversion", "Yards(yd) to Meters(m) conversion",]
    
    enumerate_menu_units_of_dimension_dict = dict(enumerate(menu_units_of_dimension_list))
    for k, v in enumerate_menu_units_of_dimension_dict.items():
        print(k, " - ", v)
    print("")
    
    while True:
        user_input = input("Your choice is: ")
        if user_input == "0":
            sleep(1)
            return phase_const.MAIN_MENU_PHASE
        elif user_input == "1":
            sleep(1)
            return subphases_const.METERS_TO_FEET
        elif user_input == "2":
            sleep(1)
            return subphases_const.FEET_TO_METERS
        elif user_input == "3":
            sleep(1)
            return subphases_const.METERS_TO_INCHES
        elif user_input == "4":
            sleep(1)
            return subphases_const.INCHES_TO_METERS
        elif user_input == "5":
            sleep(1)
            return subphases_const.CENTIMETERS_TO_INCHES
        elif user_input == "6":
            sleep(1)
            return subphases_const.INCHES_TO_CENTIMETERS
        elif user_input == "7":
            sleep(1)
            return subphases_const.KILOMETERS_TO_MILES
        elif user_input == "8":
            sleep(1)
            return subphases_const.MILES_TO_KILOMETERS
        elif user_input == "9":
            sleep(1)
            return subphases_const.METERS_TO_YARDS
        elif user_input == "10":
            sleep(1)
            return subphases_const.YARDS_TO_METERS
        else:
            print("Out of range.")
            continue
