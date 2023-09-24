import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def meters_to_inches():
    print("\n\n\tMETERS(m) to INCHES(in) conversion\n" + SEPARATOR)
    print("You have chosen dimension units for conversion, specifically Meters(m) units to Inches(in) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Meters(m) to Inches(in)?")
        
        secret_meters_to_inches_formula_dict = {"0": "NO and go straight to dimension units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_meters_to_inches_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Meters(m) to Inches(in) --->\nInches(in) = Meters(m) * 39.3701\n1 meter(m) is equal to 39.3701 inches(in).\nUse this formula to convert 1.5 meters(m) to inches(in): 59.06(in) = 1.5(m) * 39.3701\n")
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
        return conversion_meters_to_inches(meters_number_input)


def conversion_meters_to_inches(meters_number_input):
    meters_number_input_string = str(meters_number_input)
    find_decimal_point_in_meters = meters_number_input_string.find(".")
    
    inches_number = meters_number_input * 39.3701
    
    inches_number_string = str(inches_number)
    find_decimal_point_in_inches = inches_number_string.find(".")
    
    if inches_number_string[find_decimal_point_in_inches+1:] == "0" and meters_number_input_string[find_decimal_point_in_meters+1:] == "0":
        inches_number_without_decimal = int(inches_number_string[:find_decimal_point_in_inches])
        meters_number_without_decimal = int(meters_number_input_string[:find_decimal_point_in_meters])
        print("\nSo, you entered a dimension unit: " + str(meters_number_without_decimal) + " meters(m), and after conversion, it's " + str(inches_number_without_decimal) + " inches(in).")
        print(str(meters_number_without_decimal) + "(m) = " + str(inches_number_without_decimal) + "(in)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_inches()
    
    elif inches_number_string[find_decimal_point_in_inches+1:] == "0" and meters_number_input_string[find_decimal_point_in_meters+1:] != "0":
        inches_number_without_decimal = int(inches_number_string[:find_decimal_point_in_inches])
        print("\nSo, you entered a dimension unit: " + str(meters_number_input) + " meters(m), and after conversion, it's " + str(inches_number_without_decimal) + " inches(in).")
        print(str(meters_number_input) + "(m) = " + str(inches_number_without_decimal) + "(in)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_inches()
    
    elif inches_number_string[find_decimal_point_in_inches+1:] != "0" and meters_number_input_string[find_decimal_point_in_meters+1:] == "0":
        meters_number_without_decimal = int(meters_number_input_string[:find_decimal_point_in_meters])
        print("\nSo, you entered a dimension unit: " + str(meters_number_without_decimal) + " meters(m), and after conversion, it's " + str(round(inches_number, 2)) + " inches(in).")
        print(str(meters_number_without_decimal) + "(m) = " + str(round(inches_number, 2)) + "(in)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_inches()
    
    else:
        print("\nSo, you entered a dimension unit: " + str(meters_number_input) + " meters(m), and after conversion, it's " + str(round(inches_number, 2)) + " inches(in).")
        print(str(meters_number_input) + "(m) = " + str(round(inches_number, 2)) + "(in)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_inches()


def end_or_repeat_conversion_meters_to_inches():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen dimension units: Meters(m) to Inches(in), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of dimension units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_dimension_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_dimension_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Meters(m) to Inches(in) program.")
            sleep(1)
            return phase_const.DIMENSION_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Meters(m) to Inches(in) units again.")
            sleep(1)
            return meters_to_inches()
        else:
            print("\nOut of range, try again!")
            continue
