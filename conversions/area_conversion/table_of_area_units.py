from conversions.area_conversion.area_units_dictionary import area_units_dict
import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def table_of_area_units():
    sleep(1)
    print("\n\n\tTABLE OF AREA UNITS\n" + SEPARATOR + "\nYou have chosen to show units of area and their possible conversions.\n" + SEPARATOR)
    sleep(1)
    
    print("\n\tIntroductory info:")
    print(SEPARATOR)
    print("Calculations cannot be done in this section.\nIt's just about displaying a table of area units and their possible conversions.")
    print("To return to the main menu and exit the table displaying area units, please enter 0\n" + SEPARATOR)
    sleep(2)
  
    for i in area_units_dict:
        print("")
        print(str(i) + ":")
        for key, value in area_units_dict[i].items():
            for k, v in value.items():
                print("\t" + str(key) + " = " + str(v))
            

    sleep(1)
    print("\n"+ SEPARATOR + "\nTo return to the main menu and exit the table displaying area units, please enter 0\n" + SEPARATOR)
    while True:
        user_input = input("Your choice is: ")
        if user_input == "0":
            sleep(1)
            return phase_const.MAIN_MENU_PHASE
        else:
            print("Out of range.")
            continue
