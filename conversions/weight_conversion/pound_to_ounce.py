import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def pound_to_ounce():
    print("\n\n\tPOUND(g) to OUNCE(oz) conversion\n" + SEPARATOR)
    print("You have chosen weight units for conversion, specifically Pound(lb) units to Ounce(oz) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Pound(lb) to Ounce(oz)?")
        
        secret_pound_to_ounce_formula_dict = {"0": "NO and go straight to weight units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_pound_to_ounce_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Pound(lb) to Ounce(oz) --->\nOunce(oz) = Pound(lb) * 16\n1 pound(lb) is equal to 16 ounces(oz).\nUse this formula to convert 5 pounds(lb) to ounce(oz): 80(oz) = 5(lb) * 16\n")
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
        return conversion_pound_to_ounce(pound_number_input)


def conversion_pound_to_ounce(pound_number_input):
    pound_number_input_string = str(pound_number_input)
    find_decimal_point_in_pound = pound_number_input_string.find(".")
    
    ounce_number = pound_number_input * 16
    
    ounce_number_string = str(ounce_number)
    find_decimal_point_in_ounce = ounce_number_string.find(".")
    
    if ounce_number_string[find_decimal_point_in_ounce+1:] == "0" and pound_number_input_string[find_decimal_point_in_pound+1:] == "0":
        ounce_number_without_decimal = int(ounce_number_string[:find_decimal_point_in_ounce])
        pound_number_without_decimal = int(pound_number_input_string[:find_decimal_point_in_pound])
        print("\nSo, you entered a weight unit: " + str(pound_number_without_decimal) + " pound(lb), and after conversion, it's " + str(ounce_number_without_decimal) + " ounce(oz).")
        print(str(pound_number_without_decimal) + "(lb) = " + str(ounce_number_without_decimal) + "(oz)")
        sleep(1)
        return end_or_repeat_conversion_pound_to_ounce()
    
    elif ounce_number_string[find_decimal_point_in_ounce+1:] == "0" and pound_number_input_string[find_decimal_point_in_pound+1:] != "0":
        ounce_number_without_decimal = int(ounce_number_string[:find_decimal_point_in_ounce])
        print("\nSo, you entered a weight unit: " + str(pound_number_input) + " pound(lb), and after conversion, it's " + str(ounce_number_without_decimal) + " ounce(oz).")
        print(str(pound_number_input) + "(lb) = " + str(ounce_number_without_decimal) + "(oz)")
        sleep(1)
        return end_or_repeat_conversion_pound_to_ounce()
    
    elif ounce_number_string[find_decimal_point_in_ounce+1:] != "0" and pound_number_input_string[find_decimal_point_in_pound+1:] == "0":
        pound_number_without_decimal = int(pound_number_input_string[:find_decimal_point_in_pound])
        print("\nSo, you entered a weight unit: " + str(pound_number_without_decimal) + " pound(lb), and after conversion, it's " + str(round(ounce_number, 2)) + " ounce(oz).")
        print(str(pound_number_without_decimal) + "(lb) = " + str(round(ounce_number, 2)) + "(oz)")
        sleep(1)
        return end_or_repeat_conversion_pound_to_ounce()
    
    else:
        print("\nSo, you entered a weight unit: " + str(pound_number_input) + " pound(lb), and after conversion, it's " + str(round(ounce_number, 2)) + " ounce(oz).")
        print(str(pound_number_input) + "(lb) = " + str(round(ounce_number, 2)) + "(oz)")
        sleep(1)
        return end_or_repeat_conversion_pound_to_ounce()
    
    
def end_or_repeat_conversion_pound_to_ounce():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen weight units: Pound(lb) to Ounce(oz), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of weight units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_weight_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_weight_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Pound(lb) to Ounce(oz) program.")
            sleep(1)
            return phase_const.WEIGHT_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Pound(lb) to Ounce(oz) units again.")
            sleep(1)
            return pound_to_ounce()
        else:
            print("\nOut of range, try again!")
            continue
