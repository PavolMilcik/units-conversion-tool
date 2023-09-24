from conversions.memory_conversion.memory_units_dictionary import memory_units_dict
import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def table_of_memory_units():
    sleep(1)
    print("\n\n\tTABLE OF MEMORY UNITS\n" + SEPARATOR + "\nYou have chosen to show units of memory and their possible conversions.\n" + SEPARATOR)
    sleep(1)
    
    print("\n\tIntroductory info:")
    print(SEPARATOR)
    print("Calculations cannot be done in this section.\nIt's just about displaying a table of memory units and their possible conversions.")
    print("To return to the main menu and exit the table displaying memory units, please enter 0\n" + SEPARATOR)
    sleep(2)
    
    for key, value in memory_units_dict.items():
        print("")
        if key == "Kilobyte(KB)":
            print(SEPARATOR)
            print("The following conversions are based on binary multiples, where each unit is 1024 times larger than the unit before it.")
            print(SEPARATOR + "\n")
        print(str(key) + ":")
        for k, v in value.items():
            if len(v) > 0:
                if isinstance(v, list):
                    for i in v:
                        print("\t" + str(i))
                else:
                    print("\t" + str(v))

    sleep(1)
    print("\n"+ SEPARATOR + "\nTo return to the main menu and exit the table displaying memory units, please enter 0\n" + SEPARATOR)
    while True:
        user_input = input("Your choice is: ")
        if user_input == "0":
            sleep(1)
            return phase_const.MAIN_MENU_PHASE
        else:
            print("Out of range.")
            continue
