from conversions.screen_resolution.screen_resolutions_dictionary import screen_resolutions_dict
import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def table_of_screen_resolutions():
    sleep(1)
    print("\n\n\tTABLE OF SCREEN RESOLUTIONS IN PIXELS\n" + SEPARATOR + "\nYou have chosen to show table of screen resolutions in pixels.\n" + SEPARATOR)
    sleep(1)
    
    print("\n\tIntroductory info:")
    print(SEPARATOR)
    print("Calculations cannot be done in this section.\nIt's about displaying a table of common screen resolutions in pixels.")
    print("To return to the main menu and exit the table displaying memory units, please enter 0\n" + SEPARATOR)
    
    sleep(1)
    print("\n" + SEPARATOR)
    print("A pixel is the smallest unit of a screen or a digital image.\nIt is a tiny square that represents a single point of color on the screen.")
    print("Screen resolutions are often expressed in pixels (e.g., 1920x1080, which means 1920 pixels wide and 1080 pixels tall).")
    print(SEPARATOR)
    sleep(2)
    
    for i in screen_resolutions_dict:
        print("")
        print(str(i) + " resolution:")
        for key, value in screen_resolutions_dict[i].items():
            print("\t" + str(key) + ": " + str(value))
            

    sleep(1)
    print("\n"+ SEPARATOR + "\nTo return to the main menu and exit the table of screen resolutions in pixels, please enter 0\n" + SEPARATOR)
    while True:
        user_input = input("Your choice is: ")
        if user_input == "0":
            sleep(1)
            return phase_const.MAIN_MENU_PHASE
        else:
            print("Out of range.")
            continue
