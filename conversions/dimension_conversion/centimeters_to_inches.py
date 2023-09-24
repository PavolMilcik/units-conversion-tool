import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def centimeters_to_inches():
    print("\n\n\tCENTIMETERS(cm) to INCHES(in) conversion\n" + SEPARATOR)
    print("You have chosen dimension units for conversion, specifically Centimeters(cm) units to Inches(in) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Centimeters(cm) to Inches(in)?")
        
        secret_centimeters_to_inches_formula_dict = {"0": "NO and go straight to dimension units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_centimeters_to_inches_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Centimeters(cm) to Inches(in) --->\nInches(in) = Centimeters(cm) * (1/2.54)\n1 centimeter(cm) is equal to 0.393701 = 1/2.54 inches(in).\nUse this formula to convert 128 centimeters(cm) to inches(in): 50.394(in) = 128(cm) * (1/2.54)\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Centimeters(cm) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_centimeters_input = input("Your Centimeters(cm) value(number) to convert is: ")
        try:
            centimeters_number_input = float(user_centimeters_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_centimeters_to_inches(centimeters_number_input)


def conversion_centimeters_to_inches(centimeters_number_input):
    centimeters_number_input_string = str(centimeters_number_input)
    find_decimal_point_in_centimeters = centimeters_number_input_string.find(".")
    
    inches_number = centimeters_number_input * (1/2.54)
    
    inches_number_string = str(inches_number)
    find_decimal_point_in_inches = inches_number_string.find(".")
    
    if inches_number_string[find_decimal_point_in_inches+1:] == "0" and centimeters_number_input_string[find_decimal_point_in_centimeters+1:] == "0":
        inches_number_without_decimal = int(inches_number_string[:find_decimal_point_in_inches])
        centimeters_number_without_decimal = int(centimeters_number_input_string[:find_decimal_point_in_centimeters])
        print("\nSo, you entered a dimension unit: " + str(centimeters_number_without_decimal) + " centimeters(cm), and after conversion, it's " + str(inches_number_without_decimal) + " inches(in).")
        print(str(centimeters_number_without_decimal) + "(cm) = " + str(inches_number_without_decimal) + "(in)")
        sleep(1)
        return end_or_repeat_conversion_centimeters_to_inches()
    
    elif inches_number_string[find_decimal_point_in_inches+1:] == "0" and centimeters_number_input_string[find_decimal_point_in_centimeters+1:] != "0":
        inches_number_without_decimal = int(inches_number_string[:find_decimal_point_in_inches])
        print("\nSo, you entered a dimension unit: " + str(centimeters_number_input) + " centimeters(cm), and after conversion, it's " + str(inches_number_without_decimal) + " inches(in).")
        print(str(centimeters_number_input) + "(cm) = " + str(inches_number_without_decimal) + "(in)")
        sleep(1)
        return end_or_repeat_conversion_centimeters_to_inches()
    
    elif inches_number_string[find_decimal_point_in_inches+1:] != "0" and centimeters_number_input_string[find_decimal_point_in_centimeters+1:] == "0":
        centimeters_number_without_decimal = int(centimeters_number_input_string[:find_decimal_point_in_centimeters])
        print("\nSo, you entered a dimension unit: " + str(centimeters_number_without_decimal) + " centimeters(cm), and after conversion, it's " + str(round(inches_number, 3)) + " inches(in).")
        print(str(centimeters_number_without_decimal) + "(cm) = " + str(round(inches_number, 3)) + "(in)")
        sleep(1)
        return end_or_repeat_conversion_centimeters_to_inches()
    
    else:
        print("\nSo, you entered a dimension unit: " + str(centimeters_number_input) + " centimeters(cm), and after conversion, it's " + str(round(inches_number, 3)) + " inches(in).")
        print(str(centimeters_number_input) + "(cm) = " + str(round(inches_number, 3)) + "(in)")
        sleep(1)
        return end_or_repeat_conversion_centimeters_to_inches()


def end_or_repeat_conversion_centimeters_to_inches():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen dimension units: Centimeters(cm) to Inches(in), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of dimension units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_dimension_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_dimension_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Centimeters(cm) to Inches(in) program.")
            sleep(1)
            return phase_const.DIMENSION_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Centimeters(cm) to Inches(in) units again.")
            sleep(1)
            return centimeters_to_inches()
        else:
            print("\nOut of range, try again!")
            continue
