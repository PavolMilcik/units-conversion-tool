import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def gallons_to_liters():
    print("\n\n\tGALLONS(US)(gal) to LITERS(l) conversion\n" + SEPARATOR)
    print("You have chosen to convert units of liquid volume, specifically Gallons(US)(gal) units to Liters(l) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Gallons(US)(gal) to Liters(l)?")
        
        secret_gallons_to_liters_formula_dict = {"0": "NO and go straight to liquid units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_gallons_to_liters_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Gallons(US)(gal) to Liters(l) --->\nLiters(l) = Gallons(US)(gal) * 3.78541\n1 gallon(US)(gal) = 3.78541 liters(l).\nUse this formula to convert 26.5 Gallons(US)(gal) to Liters(l): 100.31(l) = 26.5(US)(gal) * 3.78541\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Gallons(US)(gal) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_gallons_input = input("Your Gallons(US)(gal) value(number) to convert is: ")
        try:
            gallons_number_input = float(user_gallons_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_gallons_to_liters(gallons_number_input)


def conversion_gallons_to_liters(gallons_number_input):
    gallons_number_input_string = str(gallons_number_input)
    find_decimal_point_in_gallons = gallons_number_input_string.find(".")
    
    liters_number = gallons_number_input * 3.78541
    
    liters_number_string = str(liters_number)
    find_decimal_point_in_liters = liters_number_string.find(".")
    
    if liters_number_string[find_decimal_point_in_liters+1:] == "0" and gallons_number_input_string[find_decimal_point_in_gallons+1:] == "0":
        liters_number_without_decimal = int(liters_number_string[:find_decimal_point_in_liters])
        gallons_number_without_decimal = int(gallons_number_input_string[:find_decimal_point_in_gallons])
        print("\nSo, you entered a liquid unit: " + str(gallons_number_without_decimal) + " gallons(US)(gal), and after conversion, it's " + str(liters_number_without_decimal) + " liters(l).")
        print(str(gallons_number_without_decimal) + "(US)(gal) = " + str(liters_number_without_decimal) + "(l)")
        sleep(1)
        return end_or_repeat_conversion_gallons_to_liters()
    
    elif liters_number_string[find_decimal_point_in_liters+1:] == "0" and gallons_number_input_string[find_decimal_point_in_gallons+1:] != "0":
        liters_number_without_decimal = int(liters_number_string[:find_decimal_point_in_liters])
        print("\nSo, you entered a liquid unit: " + str(gallons_number_input) + " gallons(US)(gal), and after conversion, it's " + str(liters_number_without_decimal) + " liters(l).")
        print(str(gallons_number_input) + "(US)(gal) = " + str(liters_number_without_decimal) + "(l)")
        sleep(1)
        return end_or_repeat_conversion_gallons_to_liters()
    
    elif liters_number_string[find_decimal_point_in_liters+1:] != "0" and gallons_number_input_string[find_decimal_point_in_gallons+1:] == "0":
        gallons_number_without_decimal = int(gallons_number_input_string[:find_decimal_point_in_gallons])
        print("\nSo, you entered a liquid unit: " + str(gallons_number_without_decimal) + " gallons(US)(gal), and after conversion, it's " + str(round(liters_number, 2)) + " liters(l).")
        print(str(gallons_number_without_decimal) + "(US)(gal) = " + str(round(liters_number, 2)) + "(l)")
        sleep(1)
        return end_or_repeat_conversion_gallons_to_liters()
    
    else:
        print("\nSo, you entered a liquid unit: " + str(gallons_number_input) + " gallons(US)(gal), and after conversion, it's " + str(round(liters_number, 2)) + " liters(l).")
        print(str(gallons_number_input) + "(US)(gal) = " + str(round(liters_number, 2)) + "(l)")
        sleep(1)
        return end_or_repeat_conversion_gallons_to_liters()


def end_or_repeat_conversion_gallons_to_liters():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen liquid units: Gallons(US)(gal) to Liters(l), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of liquid units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_liquid_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_liquid_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Gallons(US)(gal) to Liters(l) program.")
            sleep(1)
            return phase_const.LIQUID_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Gallons(US)(gal) to Liters(l) units again.")
            sleep(1)
            return gallons_to_liters()
        else:
            print("\nOut of range, try again!")
            continue
