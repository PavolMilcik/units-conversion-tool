# I did not use this in the program --->

# from phases_and_constants.other_constants import SEPARATOR
# import phases_and_constants.phase_constants as phase_const
# import phases_and_constants.subphases_constants as subphases_const
# from time import sleep


# def memory_conversion_menu():
#     sleep(1)
#     print("\n\n\tMEMORY CONVERSION MENU\n" + SEPARATOR + "\nYou have chosen to convert units of memory.\n" + SEPARATOR)
    
#     print("Introductory info:")
#     print("It's just about displaying a table of memory units and their possible conversions.\nCalculations cannot be done in this section.\n")
    
#     menu_memory_list = ["Go back to main menu", "Bit(b) conversion", "Byte(B) conversion", "Kilobyte(KB) conversion", "Megabyte(MB) conversion", "Gigabyte(GB) conversion", "Terabyte(TB) conversion", "Petabyte(PB) conversion", "Exabyte(EB) conversion", "Zettabyte(ZB) conversion", "Yottabyte(YB) conversion",]
    
#     enumerate_menu_memory_dict = dict(enumerate(menu_memory_list))
#     for k, v in enumerate_menu_memory_dict.items():
#         print(k, " - ", v)
#     print("")
    
#     while True:
#         user_input = input("Your choice is: ")
#         if user_input == "0":
#             sleep(1)
#             return phase_const.MAIN_MENU_PHASE
#         elif user_input == "1":
#             sleep(1)
#             return subphases_const.BIT
#         elif user_input == "2":
#             sleep(1)
#             return subphases_const.BYTE
#         elif user_input == "3":
#             sleep(1)
#             return subphases_const.KILOBYTE
#         elif user_input == "4":
#             sleep(1)
#             return subphases_const.MEGABYTE
#         elif user_input == "5":
#             sleep(1)
#             return subphases_const.GIGABYTE
#         elif user_input == "6":
#             sleep(1)
#             return subphases_const.TERABYTE
#         elif user_input == "7":
#             sleep(1)
#             return subphases_const.PETABYTE
#         elif user_input == "8":
#             sleep(1)
#             return subphases_const.EXABYTE
#         elif user_input == "9":
#             sleep(1)
#             return subphases_const.ZETTABYTE
#         elif user_input == "10":
#             sleep(1)
#             return subphases_const.YOTTABYTE
#         else:
#             print("Out of range.")
#             continue
