import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def menu_selection():
    print("\n\n\tMAIN MENU\n" + SEPARATOR + "\nYou have a choice of the following conversions. --->\n" + SEPARATOR)
    sleep(1)

    menu_list = ["End the conversion program", "Temperature degrees conversions (°F, °C)", "Weight units and their conversions (oz, g, lb, kg, t)", "Liquid volume conversions (l, ml, gal(US), fl oz, cubic m, US bbl oil)", "Dimension units (such as length, width, height, or distance) and their conversions (m, ft, in, cm, mi, km, yd)", "Speed units conversions (km/h, m/s, mph, kn or kt)", "Area units and their conversions (square m, square ft, ha, ac, square km, square mi)", "Memory units and their conversions (b, B, KB, MB, GB, TB, PB, EB, ZB, YB)", "Screen resolutions in pixels (HD, Full HD, 2K, 4K, 8K)"]
    
    enumerate_menu_dict = dict(enumerate(menu_list))
    for k, v in enumerate_menu_dict.items():
        print(k, " - ", v)
    print("")
    
    while True:
        sleep(1)
        user_menu_selection_input = input("Which conversion option will you choose: ")
        if user_menu_selection_input == "0":
            sleep(1)
            return phase_const.END_CONVERSION_PROGRAM
        elif user_menu_selection_input == "1":
            sleep(1)
            return phase_const.TEMPERATURE_CONVERSION_MENU
        elif user_menu_selection_input == "2":
            sleep(1)
            return phase_const.WEIGHT_CONVERSION_MENU
        elif user_menu_selection_input == "3":
            sleep(1)
            return phase_const.LIQUID_CONVERSION_MENU
        elif user_menu_selection_input == "4":
            sleep(1)
            return phase_const.DIMENSION_CONVERSION_MENU
        elif user_menu_selection_input == "5":
            sleep(1)
            return phase_const.SPEED_CONVERSION_MENU
        elif user_menu_selection_input == "6":
            sleep(1)
            return phase_const.AREA_CONVERSION_TABLE
        elif user_menu_selection_input == "7":
            sleep(1)
            return phase_const.MEMORY_CONVERSION_TABLE
        elif user_menu_selection_input == "8":
            sleep(1)
            return phase_const.SCREEN_RESOLUTIONS_TABLE
        else:
            print("Out of range, try again!\n")
            continue  
