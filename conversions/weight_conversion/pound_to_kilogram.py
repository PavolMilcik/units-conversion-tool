import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def pound_to_kilogram():
    print("\n\n\tPOUND(lb) to KILOGRAM(kg) conversion\n" + SEPARATOR)
    print("You have chosen weight units for conversion, specifically Pound(lb) units to Kilogram(kg) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Pound(lb) to Kilogram(kg)?")
        
        secret_pound_to_kilogram_formula_dict = {"0": "NO and go straight to weight units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_pound_to_kilogram_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Pound(lb) to Kilogram(kg) --->\nKilograms(kg) = Pound(lb) * 0.453592\n1 pound(lb) is approximately equal to 0.453592 kilograms(kg).\nUse this formula to convert 168 pound(lb) to kilograms(kg): 76.2(kg) = 168(lb) * 0.453592\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Pound(lb) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_pound_input = input("Your Pound(lb) value(number) to convert is: ")
        try:
            pound_number_input = float(user_pound_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_pound_to_kilogram(pound_number_input)


def conversion_pound_to_kilogram(pound_number_input):
    pound_number_input_string = str(pound_number_input)
    find_decimal_point_in_pound = pound_number_input_string.find(".")
    
    kilogram_number = pound_number_input * 0.453592
    
    kilogram_number_string = str(kilogram_number)
    find_decimal_point_in_kilogram = kilogram_number_string.find(".")
    
    if kilogram_number_string[find_decimal_point_in_kilogram+1:] == "0" and pound_number_input_string[find_decimal_point_in_pound+1:] == "0":
        kilogram_number_without_decimal = int(kilogram_number_string[:find_decimal_point_in_kilogram])
        pound_number_without_decimal = int(pound_number_input_string[:find_decimal_point_in_pound])
        print("\nSo, you entered a weight unit: " + str(pound_number_without_decimal) + " pound(lb), and after conversion, it's " + str(kilogram_number_without_decimal) + " kilogram(kg).")
        print(str(pound_number_without_decimal) + "(lb) = " + str(kilogram_number_without_decimal) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_pound_to_kilogram()
    
    elif kilogram_number_string[find_decimal_point_in_kilogram+1:] == "0" and pound_number_input_string[find_decimal_point_in_pound+1:] != "0":
        kilogram_number_without_decimal = int(kilogram_number_string[:find_decimal_point_in_kilogram])
        print("\nSo, you entered a weight unit: " + str(pound_number_input) + " pound(lb), and after conversion, it's " + str(kilogram_number_without_decimal) + " kilogram(kg).")
        print(str(pound_number_input) + "(lb) = " + str(kilogram_number_without_decimal) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_pound_to_kilogram()
    
    elif kilogram_number_string[find_decimal_point_in_kilogram+1:] != "0" and pound_number_input_string[find_decimal_point_in_pound+1:] == "0":
        pound_number_without_decimal = int(pound_number_input_string[:find_decimal_point_in_pound])
        print("\nSo, you entered a weight unit: " + str(pound_number_without_decimal) + " pound(lb), and after conversion, it's " + str(round(kilogram_number, 1)) + " kilogram(kg).")
        print(str(pound_number_without_decimal) + "(lb) = " + str(round(kilogram_number, 1)) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_pound_to_kilogram()
    
    else:
        print("\nSo, you entered a weight unit: " + str(pound_number_input) + " pound(lb), and after conversion, it's " + str(round(kilogram_number, 1)) + " kilogram(kg).")
        print(str(pound_number_input) + "(lb) = " + str(round(kilogram_number, 1)) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_pound_to_kilogram()
    
    
def end_or_repeat_conversion_pound_to_kilogram():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen weight units: Pound(lb) to Kilogram(kg), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of weight units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_weight_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_weight_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Pound(lb) to Kilogram(kg) program.")
            sleep(1)
            return phase_const.WEIGHT_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Pound(lb) to Kilogram(kg) units again.")
            sleep(1)
            return pound_to_kilogram()
        else:
            print("\nOut of range, try again!")
            continue
