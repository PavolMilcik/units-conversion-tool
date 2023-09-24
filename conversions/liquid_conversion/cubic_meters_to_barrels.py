import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def cubic_meters_to_barrels():
    print("\n\n\tCUBIC METERS(cubic m) to BARRELS(US bbl oil) conversion\n" + SEPARATOR)
    print("You have chosen to convert units of liquid volume, specifically Cubic Meters(cubic m) units to Barrels(US bbl oil) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Cubic Meters(cubic m) to Barrels(US bbl oil)?")
        
        secret_cubic_meters_to_barrels_formula_dict = {"0": "NO and go straight to liquid units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_cubic_meters_to_barrels_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Cubic Meters(cubic m) to Barrels(US bbl oil) --->\nBarrels(US bbl oil) = Cubic Meters(cubic m) * 6.28981\n1 cubic meter(m³) is approximately equal to 6.28981 barrels(US bbl oil).\nUse this formula to convert 2 cubic meters(cubic m) to barrels(US bbl oil): 12.58(US bbl oil) = 2(cubic m) * 6.28981\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Cubic Meters(cubic m) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_cubic_meters_input = input("Your Cubic Meters(cubic m) value(number) to convert is: ")
        try:
            cubic_meters_number_input = float(user_cubic_meters_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_cubic_meters_to_barrels(cubic_meters_number_input)


def conversion_cubic_meters_to_barrels(cubic_meters_number_input):
    cubic_meters_number_input_string = str(cubic_meters_number_input)
    find_decimal_point_in_cubic_meters = cubic_meters_number_input_string.find(".")
    
    barrels_number = cubic_meters_number_input * 6.28981
    
    barrels_number_string = str(barrels_number)
    find_decimal_point_in_barrels = barrels_number_string.find(".")
    
    if barrels_number_string[find_decimal_point_in_barrels+1:] == "0" and cubic_meters_number_input_string[find_decimal_point_in_cubic_meters+1:] == "0":
        barrels_number_without_decimal = int(barrels_number_string[:find_decimal_point_in_barrels])
        cubic_meters_number_without_decimal = int(cubic_meters_number_input_string[:find_decimal_point_in_cubic_meters])
        print("\nSo, you entered a liquid unit: " + str(cubic_meters_number_without_decimal) + " cubic_meters(cubic m), and after conversion, it's " + str(barrels_number_without_decimal) + " barrels(US bbl oil).")
        print(str(cubic_meters_number_without_decimal) + "(cubic m) = " + str(barrels_number_without_decimal) + "(US bbl oil)")
        sleep(1)
        return end_or_repeat_conversion_cubic_meters_to_barrels()
    
    elif barrels_number_string[find_decimal_point_in_barrels+1:] == "0" and cubic_meters_number_input_string[find_decimal_point_in_cubic_meters+1:] != "0":
        barrels_number_without_decimal = int(barrels_number_string[:find_decimal_point_in_barrels])
        print("\nSo, you entered a liquid unit: " + str(cubic_meters_number_input) + " cubic_meters(cubic m), and after conversion, it's " + str(barrels_number_without_decimal) + " barrels(US bbl oil).")
        print(str(cubic_meters_number_input) + "(cubic m) = " + str(barrels_number_without_decimal) + "(US bbl oil)")
        sleep(1)
        return end_or_repeat_conversion_cubic_meters_to_barrels()
    
    elif barrels_number_string[find_decimal_point_in_barrels+1:] != "0" and cubic_meters_number_input_string[find_decimal_point_in_cubic_meters+1:] == "0":
        cubic_meters_number_without_decimal = int(cubic_meters_number_input_string[:find_decimal_point_in_cubic_meters])
        print("\nSo, you entered a liquid unit: " + str(cubic_meters_number_without_decimal) + " cubic_meters(cubic m), and after conversion, it's " + str(round(barrels_number, 2)) + " barrels(US bbl oil).")
        print(str(cubic_meters_number_without_decimal) + "(cubic m) = " + str(round(barrels_number, 2)) + "(US bbl oil)")
        sleep(1)
        return end_or_repeat_conversion_cubic_meters_to_barrels()
    
    else:
        print("\nSo, you entered a liquid unit: " + str(cubic_meters_number_input) + " cubic_meters(cubic m), and after conversion, it's " + str(round(barrels_number, 2)) + " barrels(US bbl oil).")
        print(str(cubic_meters_number_input) + "(cubic m) = " + str(round(barrels_number, 2)) + "(US bbl oil)")
        sleep(1)
        return end_or_repeat_conversion_cubic_meters_to_barrels()


def end_or_repeat_conversion_cubic_meters_to_barrels():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen liquid units: Cubic Meters(cubic m) to Barrels(US bbl oil), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of liquid units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_liquid_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_liquid_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Cubic Meters(cubic m) to Barrels(US bbl oil) program.")
            sleep(1)
            return phase_const.LIQUID_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Cubic Meters(cubic m) to Barrels(US bbl oil) units again.")
            sleep(1)
            return cubic_meters_to_barrels()
        else:
            print("\nOut of range, try again!")
            continue
