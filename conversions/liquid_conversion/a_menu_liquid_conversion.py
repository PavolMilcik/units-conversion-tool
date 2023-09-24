from phases_and_constants.other_constants import SEPARATOR
import phases_and_constants.phase_constants as phase_const
import phases_and_constants.subphases_constants as subphases_const
from time import sleep


def liquid_conversion_menu():
    sleep(1)
    print("\n\n\tLIQUID VOLUME CONVERSION MENU\n" + SEPARATOR + "\nYou have chosen to convert units of liquid volume. But first, choose what you want to convert to what.\n" + SEPARATOR)
    menu_units_of_liquid_list = ["Go back to main menu", "Liters(l) to Milliliters(ml) conversion", "Milliliters(ml) to Liters(l) conversion", "Gallons(US)(gal) to Liters(l) conversion", "Liters(l) to Gallons(US)(gal) conversion", "Fluid Ounces(US)(fl oz) to Milliliters(ml) conversion", "Milliliters(mL) to Fluid Ounces(US)(fl oz) conversion", "Cubic Meters(m³) to Liters(L) conversion", "Liters(L) to Cubic Meters(m³) conversion", "Barrels(US bbl oil) to Cubic Meters(m³) conversion", "Cubic Meters(m³) to Barrels(US bbl oil) conversion",]
    
    enumerate_menu_units_of_liquid_dict = dict(enumerate(menu_units_of_liquid_list))
    for k, v in enumerate_menu_units_of_liquid_dict.items():
        print(k, " - ", v)
    print("")
    
    while True:
        user_input = input("Your choice is: ")
        if user_input == "0":
            sleep(1)
            return phase_const.MAIN_MENU_PHASE
        elif user_input == "1":
            sleep(1)
            return subphases_const.LITERS_TO_MILLILITERS
        elif user_input == "2":
            sleep(1)
            return subphases_const.MILLILITERS_TO_LITERS
        elif user_input == "3":
            sleep(1)
            return subphases_const.GALLONS_TO_LITERS
        elif user_input == "4":
            sleep(1)
            return subphases_const.LITERS_TO_GALLONS
        elif user_input == "5":
            sleep(1)
            return subphases_const.FLUID_OUNCES_TO_MILLILITERS
        elif user_input == "6":
            sleep(1)
            return subphases_const.MILLILITERS_TO_FLUID_OUNCES
        elif user_input == "7":
            sleep(1)
            return subphases_const.CUBIC_METERS_TO_LITERS
        elif user_input == "8":
            sleep(1)
            return subphases_const.LITERS_TO_CUBIC_METERS
        elif user_input == "9":
            sleep(1)
            return subphases_const.BARRELS_TO_CUBIC_METERS
        elif user_input == "10":
            sleep(1)
            return subphases_const.CUBIC_METERS_TO_BARRELS
        else:
            print("Out of range.")
            continue
