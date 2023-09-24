# I did not use this in the program --->

# from phases_and_constants.other_constants import SEPARATOR
# import phases_and_constants.phase_constants as phase_const
# import phases_and_constants.subphases_constants as subphases_const
# from time import sleep


# def area_conversion_menu():
#     sleep(1)
#     print("\n\n\tAREA CONVERSION MENU\n" + SEPARATOR + "\nYou have chosen to convert units of area.\n" + SEPARATOR)
    
#     print("Introductory info:")
#     print("It's just about displaying a table of area units and their possible conversions.\nCalculations cannot be done in this section.\n" + SEPARATOR + "\n")
    
#     menu_area_list = ["Go back to main menu", "Square Meter(m²) conversion", "Square Foot(ft²) conversion", "Square Kilometer(km²) conversion", "Square Mile(mi²) conversion", "Hectare(ha) conversion", "Acre(ac) conversion", "Square yard(yd²) conversion"]
    
#     enumerate_menu_area_dict = dict(enumerate(menu_area_list))
#     for k, v in enumerate_menu_area_dict.items():
#         print(k, " - ", v)
#     print("")
    
#     while True:
#         user_input = input("Your choice is: ")
#         if user_input == "0":
#             sleep(1)
#             return phase_const.MAIN_MENU_PHASE
#         elif user_input == "1":
#             sleep(1)
#             return subphases_const.SQUARE_METER
#         elif user_input == "2":
#             sleep(1)
#             return subphases_const.SQUARE_FOOT
#         elif user_input == "3":
#             sleep(1)
#             return subphases_const.SQUARE_KILOMETER
#         elif user_input == "4":
#             sleep(1)
#             return subphases_const.SQUARE_MILE
#         elif user_input == "5":
#             sleep(1)
#             return subphases_const.HECTARE
#         elif user_input == "6":
#             sleep(1)
#             return subphases_const.ACRE
#         elif user_input == "7":
#             sleep(1)
#             return subphases_const.SQUARE_YARDS
#         else:
#             print("Out of range.")
#             continue
