from phases_and_constants.other_constants import SEPARATOR
import phases_and_constants.phase_constants as phase_const
import phases_and_constants.subphases_constants as subphases_const
from time import sleep


def speed_conversion_menu():
    sleep(1)
    print("\n\n\tSPEED CONVERSION MENU\n" + SEPARATOR + "\nYou have chosen to convert units of speed. But first, choose what you want to convert to what.\n" + SEPARATOR)
    menu_speed_list = ["Go back to main menu", "Kilometers per Hour(km/h) to Meters per Second(m/s) conversion", "Meters per Second(m/s) to Kilometers per Hour(km/h) conversion", "Kilometers per Hour(km/h) to Miles per Hour(mph) conversion", "Miles per Hour(mph) to  Kilometers per Hour(km/h) conversion", "Kilometers per Hour(km/h) to Knots(kn or kt) conversion", "Knots(kn or kt) to Kilometers per Hour(km/h) conversion"]
    
    enumerate_menu_speed_dict = dict(enumerate(menu_speed_list))
    for k, v in enumerate_menu_speed_dict.items():
        print(k, " - ", v)
    print("")
    
    while True:
        user_input = input("Your choice is: ")
        if user_input == "0":
            sleep(1)
            return phase_const.MAIN_MENU_PHASE
        elif user_input == "1":
            sleep(1)
            return subphases_const.KILOMETERS_PER_HOUR_TO_METERS_PER_SECOND
        elif user_input == "2":
            sleep(1)
            return subphases_const.METERS_PER_SECOND_TO_KILOMETERS_PER_HOUR
        elif user_input == "3":
            sleep(1)
            return subphases_const.KILOMETERS_PER_HOUR_TO_MILES_PER_HOUR
        elif user_input == "4":
            sleep(1)
            return subphases_const.MILES_PER_HOUR_TO_KILOMETERS_PER_HOUR
        elif user_input == "5":
            sleep(1)
            return subphases_const.KILOMETERS_PER_HOUR_TO_KNOTS
        elif user_input == "6":
            sleep(1)
            return subphases_const.KNOTS_TO_KILOMETERS_PER_HOUR
        else:
            print("Out of range.")
            continue
