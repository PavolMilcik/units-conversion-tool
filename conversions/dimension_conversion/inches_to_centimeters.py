import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def inches_to_centimeters():
    print("\n\n\tINCHES(in) to CENTIMETERS(cm) conversion\n" + SEPARATOR)
    print("You have chosen dimension units for conversion, specifically Inches(in) units to Centimeters(cm) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Inches(in) to Centimeters(cm)?")
        
        secret_inches_to_centimeters_formula_dict = {"0": "NO and go straight to dimension units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_inches_to_centimeters_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Inches(in) to Centimeters(cm) --->\nCentimeters(cm) = Inches(in) * 2.54 \n1 inch(in) is equal to 2.54 centimeters(cm).\nUse this formula to convert 7.2 inches(in) to centimeters(cm): 18.29(cm) = 7.2(in) * 2.54 \n")
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
        return conversion_inches_to_centimeters(inches_number_input)


def conversion_inches_to_centimeters(inches_number_input):
    inches_number_input_string = str(inches_number_input)
    find_decimal_point_in_inches = inches_number_input_string.find(".")
    
    centimeters_number = inches_number_input * 2.54
    
    centimeters_number_string = str(centimeters_number)
    find_decimal_point_in_centimeters = centimeters_number_string.find(".")
    
    if centimeters_number_string[find_decimal_point_in_centimeters+1:] == "0" and inches_number_input_string[find_decimal_point_in_inches+1:] == "0":
        centimeters_number_without_decimal = int(centimeters_number_string[:find_decimal_point_in_centimeters])
        inches_number_without_decimal = int(inches_number_input_string[:find_decimal_point_in_inches])
        print("\nSo, you entered a dimension unit: " + str(inches_number_without_decimal) + " inches(in), and after conversion, it's " + str(centimeters_number_without_decimal) + " centimeters(cm).")
        print(str(inches_number_without_decimal) + "(in) = " + str(centimeters_number_without_decimal) + "(cm)")
        sleep(1)
        return end_or_repeat_conversion_inches_to_centimeters()
    
    elif centimeters_number_string[find_decimal_point_in_centimeters+1:] == "0" and inches_number_input_string[find_decimal_point_in_inches+1:] != "0":
        centimeters_number_without_decimal = int(centimeters_number_string[:find_decimal_point_in_centimeters])
        print("\nSo, you entered a dimension unit: " + str(inches_number_input) + " inches(in), and after conversion, it's " + str(centimeters_number_without_decimal) + " centimeters(cm).")
        print(str(inches_number_input) + "(in) = " + str(centimeters_number_without_decimal) + "(cm)")
        sleep(1)
        return end_or_repeat_conversion_inches_to_centimeters()
    
    elif centimeters_number_string[find_decimal_point_in_centimeters+1:] != "0" and inches_number_input_string[find_decimal_point_in_inches+1:] == "0":
        inches_number_without_decimal = int(inches_number_input_string[:find_decimal_point_in_inches])
        print("\nSo, you entered a dimension unit: " + str(inches_number_without_decimal) + " inches(in), and after conversion, it's " + str(round(centimeters_number, 2)) + " centimeters(cm).")
        print(str(inches_number_without_decimal) + "(in) = " + str(round(centimeters_number, 2)) + "(cm)")
        sleep(1)
        return end_or_repeat_conversion_inches_to_centimeters()
    
    else:
        print("\nSo, you entered a dimension unit: " + str(inches_number_input) + " inches(in), and after conversion, it's " + str(round(centimeters_number, 2)) + " centimeters(cm).")
        print(str(inches_number_input) + "(in) = " + str(round(centimeters_number, 2)) + "(cm)")
        sleep(1)
        return end_or_repeat_conversion_inches_to_centimeters()


def end_or_repeat_conversion_inches_to_centimeters():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen dimension units: Inches(in) to Centimeters(cm), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of dimension units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_dimension_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_dimension_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Inches(in) to Centimeters(cm) program.")
            sleep(1)
            return phase_const.DIMENSION_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Inches(in) to Centimeters(cm) units again.")
            sleep(1)
            return inches_to_centimeters()
        else:
            print("\nOut of range, try again!")
            continue
