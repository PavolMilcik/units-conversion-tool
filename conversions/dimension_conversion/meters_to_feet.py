import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def meters_to_feet():
    print("\n\n\tMETERS(m) to FEET(ft) conversion\n" + SEPARATOR)
    print("You have chosen dimension units for conversion, specifically Meters(m) units to Feet(ft) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Meters(m) to Feet(ft)?")
        
        secret_meters_to_feet_formula_dict = {"0": "NO and go straight to dimension units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_meters_to_feet_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Meters(m) to Feet(ft) --->\nFeet(ft) = Meters(m) * 3.28084\n1 meter(m) is approximately equal to 3.28084 feet(ft).\nUse this formula to convert 8 meters(m) to feet(ft): 26.25(ft) = 8(m) * 3.28084\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Meters(m) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_meters_input = input("Your Meters(m) value(number) to convert is: ")
        try:
            meters_number_input = float(user_meters_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_meters_to_feet(meters_number_input)


def conversion_meters_to_feet(meters_number_input):
    meters_number_input_string = str(meters_number_input)
    find_decimal_point_in_meters = meters_number_input_string.find(".")
    
    feet_number = meters_number_input * 3.28084
    
    feet_number_string = str(feet_number)
    find_decimal_point_in_feet = feet_number_string.find(".")
    
    if feet_number_string[find_decimal_point_in_feet+1:] == "0" and meters_number_input_string[find_decimal_point_in_meters+1:] == "0":
        feet_number_without_decimal = int(feet_number_string[:find_decimal_point_in_feet])
        meters_number_without_decimal = int(meters_number_input_string[:find_decimal_point_in_meters])
        print("\nSo, you entered a dimension unit: " + str(meters_number_without_decimal) + " meters(m), and after conversion, it's " + str(feet_number_without_decimal) + " feet(ft).")
        print(str(meters_number_without_decimal) + "(m) = " + str(feet_number_without_decimal) + "(ft)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_feet()
    
    elif feet_number_string[find_decimal_point_in_feet+1:] == "0" and meters_number_input_string[find_decimal_point_in_meters+1:] != "0":
        feet_number_without_decimal = int(feet_number_string[:find_decimal_point_in_feet])
        print("\nSo, you entered a dimension unit: " + str(meters_number_input) + " meters(m), and after conversion, it's " + str(feet_number_without_decimal) + " feet(ft).")
        print(str(meters_number_input) + "(m) = " + str(feet_number_without_decimal) + "(ft)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_feet()
    
    elif feet_number_string[find_decimal_point_in_feet+1:] != "0" and meters_number_input_string[find_decimal_point_in_meters+1:] == "0":
        meters_number_without_decimal = int(meters_number_input_string[:find_decimal_point_in_meters])
        print("\nSo, you entered a dimension unit: " + str(meters_number_without_decimal) + " meters(m), and after conversion, it's " + str(round(feet_number, 2)) + " feet(ft).")
        print(str(meters_number_without_decimal) + "(m) = " + str(round(feet_number, 2)) + "(ft)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_feet()
    
    else:
        print("\nSo, you entered a dimension unit: " + str(meters_number_input) + " meters(m), and after conversion, it's " + str(round(feet_number, 2)) + " feet(ft).")
        print(str(meters_number_input) + "(m) = " + str(round(feet_number, 2)) + "(ft)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_feet()


def end_or_repeat_conversion_meters_to_feet():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen dimension units: Meters(m) to Feet(ft), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of dimension units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_dimension_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_dimension_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Meters(m) to Feet(ft) program.")
            sleep(1)
            return phase_const.DIMENSION_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Meters(m) to Feet(ft) units again.")
            sleep(1)
            return meters_to_feet()
        else:
            print("\nOut of range, try again!")
            continue
