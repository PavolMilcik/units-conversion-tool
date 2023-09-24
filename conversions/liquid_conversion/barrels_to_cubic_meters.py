import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def barrels_to_cubic_meters():
    print("\n\n\tBARRELS(US bbl oil) to CUBIC METERS(cubic m) conversion\n" + SEPARATOR)
    print("You have chosen to convert units of liquid volume, specifically Barrels(US bbl oil) units to Cubic Meters(cubic m) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Barrels(US bbl oil) to Cubic Meters(cubic m)?")
        
        secret_barrels_to_cubic_meters_formula_dict = {"0": "NO and go straight to liquid units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_barrels_to_cubic_meters_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Barrels(US bbl oil) to Cubic Meters(cubic m) --->\nCubic Meters(cubic m) = Barrels(US bbl oil) * (1/6.28981)\n1 barrel(bbl) is approximately equal to 0.1589873 = 1/6.28981 cubic meters(m³).\nUse this formula to convert 100 barrels(US bbl oil) to cubic meters(cubic m): 15.899(cubic m) = 100(US bbl oil) * (1/6.28981)\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Barrels(US bbl oil) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_barrels_input = input("Your Barrels(US bbl oil) value(number) to convert is: ")
        try:
            barrels_number_input = float(user_barrels_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_barrels_to_cubic_meters(barrels_number_input)


def conversion_barrels_to_cubic_meters(barrels_number_input):
    barrels_number_input_string = str(barrels_number_input)
    find_decimal_point_in_barrels = barrels_number_input_string.find(".")
    
    cubic_meters_number = barrels_number_input * (1/6.28981)
    
    cubic_meters_number_string = str(cubic_meters_number)
    find_decimal_point_in_cubic_meters = cubic_meters_number_string.find(".")
    
    if cubic_meters_number_string[find_decimal_point_in_cubic_meters+1:] == "0" and barrels_number_input_string[find_decimal_point_in_barrels+1:] == "0":
        cubic_meters_number_without_decimal = int(cubic_meters_number_string[:find_decimal_point_in_cubic_meters])
        barrels_number_without_decimal = int(barrels_number_input_string[:find_decimal_point_in_barrels])
        print("\nSo, you entered a liquid unit: " + str(barrels_number_without_decimal) + " barrels(US bbl oil), and after conversion, it's " + str(cubic_meters_number_without_decimal) + " cubic_meters(cubic m).")
        print(str(barrels_number_without_decimal) + "(US bbl oil) = " + str(cubic_meters_number_without_decimal) + "(cubic m)")
        sleep(1)
        return end_or_repeat_conversion_barrels_to_cubic_meters()
    
    elif cubic_meters_number_string[find_decimal_point_in_cubic_meters+1:] == "0" and barrels_number_input_string[find_decimal_point_in_barrels+1:] != "0":
        cubic_meters_number_without_decimal = int(cubic_meters_number_string[:find_decimal_point_in_cubic_meters])
        print("\nSo, you entered a liquid unit: " + str(barrels_number_input) + " barrels(US bbl oil), and after conversion, it's " + str(cubic_meters_number_without_decimal) + " cubic_meters(cubic m).")
        print(str(barrels_number_input) + "(US bbl oil) = " + str(cubic_meters_number_without_decimal) + "(cubic m)")
        sleep(1)
        return end_or_repeat_conversion_barrels_to_cubic_meters()
    
    elif cubic_meters_number_string[find_decimal_point_in_cubic_meters+1:] != "0" and barrels_number_input_string[find_decimal_point_in_barrels+1:] == "0":
        barrels_number_without_decimal = int(barrels_number_input_string[:find_decimal_point_in_barrels])
        print("\nSo, you entered a liquid unit: " + str(barrels_number_without_decimal) + " barrels(US bbl oil), and after conversion, it's " + str(round(cubic_meters_number, 3)) + " cubic_meters(cubic m).")
        print(str(barrels_number_without_decimal) + "(US bbl oil) = " + str(round(cubic_meters_number, 3)) + "(cubic m)")
        sleep(1)
        return end_or_repeat_conversion_barrels_to_cubic_meters()
    
    else:
        print("\nSo, you entered a liquid unit: " + str(barrels_number_input) + " barrels(US bbl oil), and after conversion, it's " + str(round(cubic_meters_number, 3)) + " cubic_meters(cubic m).")
        print(str(barrels_number_input) + "(US bbl oil) = " + str(round(cubic_meters_number, 3)) + "(cubic m)")
        sleep(1)
        return end_or_repeat_conversion_barrels_to_cubic_meters()


def end_or_repeat_conversion_barrels_to_cubic_meters():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen liquid units: Barrels(US bbl oil) to Cubic Meters(cubic m), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of liquid units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_liquid_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_liquid_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Barrels(US bbl oil) to Cubic Meters(cubic m) program.")
            sleep(1)
            return phase_const.LIQUID_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Barrels(US bbl oil) to Cubic Meters(cubic m) units again.")
            sleep(1)
            return barrels_to_cubic_meters()
        else:
            print("\nOut of range, try again!")
            continue
