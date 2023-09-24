import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def inches_to_meters():
    print("\n\n\tINCHES(in) to METERS(m) conversion\n" + SEPARATOR)
    print("You have chosen dimension units for conversion, specifically Inches(in) units to Meters(m) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Inches(in) to Meters(m)?")
        
        secret_inches_to_meters_formula_dict = {"0": "NO and go straight to dimension units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_inches_to_meters_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Inches(in) to Meters(m) --->\nMeters(m) = Inches(in) * (1/39.3701)\n1 inch(in) is equal to 0.0254 = 1/39.3701 meters(m).\nUse this formula to convert 6 inches(in) to meters(m): 0.1524(m) = 6(in) * (1/39.3701)\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Inches(in) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_inches_input = input("Your Inches(in) value(number) to convert is: ")
        try:
            inches_number_input = float(user_inches_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_inches_to_meters(inches_number_input)


def conversion_inches_to_meters(inches_number_input):
    inches_number_input_string = str(inches_number_input)
    find_decimal_point_in_inches = inches_number_input_string.find(".")
    
    meters_number = inches_number_input * (1/39.3701)
    
    meters_number_string = str(meters_number)
    find_decimal_point_in_meters = meters_number_string.find(".")
    
    if meters_number_string[find_decimal_point_in_meters+1:] == "0" and inches_number_input_string[find_decimal_point_in_inches+1:] == "0":
        meters_number_without_decimal = int(meters_number_string[:find_decimal_point_in_meters])
        inches_number_without_decimal = int(inches_number_input_string[:find_decimal_point_in_inches])
        print("\nSo, you entered a dimension unit: " + str(inches_number_without_decimal) + " inches(in), and after conversion, it's " + str(meters_number_without_decimal) + " meters(m).")
        print(str(inches_number_without_decimal) + "(in) = " + str(meters_number_without_decimal) + "(m)")
        sleep(1)
        return end_or_repeat_conversion_inches_to_meters()
    
    elif meters_number_string[find_decimal_point_in_meters+1:] == "0" and inches_number_input_string[find_decimal_point_in_inches+1:] != "0":
        meters_number_without_decimal = int(meters_number_string[:find_decimal_point_in_meters])
        print("\nSo, you entered a dimension unit: " + str(inches_number_input) + " inches(in), and after conversion, it's " + str(meters_number_without_decimal) + " meters(m).")
        print(str(inches_number_input) + "(in) = " + str(meters_number_without_decimal) + "(m)")
        sleep(1)
        return end_or_repeat_conversion_inches_to_meters()
    
    elif meters_number_string[find_decimal_point_in_meters+1:] != "0" and inches_number_input_string[find_decimal_point_in_inches+1:] == "0":
        inches_number_without_decimal = int(inches_number_input_string[:find_decimal_point_in_inches])
        print("\nSo, you entered a dimension unit: " + str(inches_number_without_decimal) + " inches(in), and after conversion, it's " + str(round(meters_number, 4)) + " meters(m).")
        print(str(inches_number_without_decimal) + "(in) = " + str(round(meters_number, 4)) + "(m)")
        sleep(1)
        return end_or_repeat_conversion_inches_to_meters()
    
    else:
        print("\nSo, you entered a dimension unit: " + str(inches_number_input) + " inches(in), and after conversion, it's " + str(round(meters_number, 4)) + " meters(m).")
        print(str(inches_number_input) + "(in) = " + str(round(meters_number, 4)) + "(m)")
        sleep(1)
        return end_or_repeat_conversion_inches_to_meters()


def end_or_repeat_conversion_inches_to_meters():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen dimension units: Inches(in) to Meters(m), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of dimension units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_dimension_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_dimension_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Inches(in) to Meters(m) program.")
            sleep(1)
            return phase_const.DIMENSION_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Inches(in) to Meters(m) units again.")
            sleep(1)
            return inches_to_meters()
        else:
            print("\nOut of range, try again!")
            continue
