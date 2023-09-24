import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def ounce_to_pound():
    print("\n\n\tOUNCE(oz) to POUND(g) conversion\n" + SEPARATOR)
    print("You have chosen weight units for conversion, specifically Ounce(oz) units to Pound(lb) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Ounce(oz) to Pound(lb)?")
        
        secret_ounce_to_pound_formula_dict = {"0": "NO and go straight to weight units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_ounce_to_pound_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Ounce(oz) to Pound(lb) --->\nPound(lb) = Ounce(oz) * (1/16)\n1 ounce(oz) is equal to 1/16 of a pound(lb).\nUse this formula to convert 80 ounce(oz) to pound(lb): 5(lb) = 80(oz) * (1/16)\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Ounce(oz) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_ounce_input = input("Your Ounce(oz) value(number) to convert is: ")
        try:
            ounce_number_input = float(user_ounce_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_ounce_to_pound(ounce_number_input)


def conversion_ounce_to_pound(ounce_number_input):
    ounce_number_input_string = str(ounce_number_input)
    find_decimal_point_in_ounce = ounce_number_input_string.find(".")
    
    pound_number = ounce_number_input * (1/16)
    
    pound_number_string = str(pound_number)
    find_decimal_point_in_pound = pound_number_string.find(".")
    
    if pound_number_string[find_decimal_point_in_pound+1:] == "0" and ounce_number_input_string[find_decimal_point_in_ounce+1:] == "0":
        pound_number_without_decimal = int(pound_number_string[:find_decimal_point_in_pound])
        ounce_number_without_decimal = int(ounce_number_input_string[:find_decimal_point_in_ounce])
        print("\nSo, you entered a weight unit: " + str(ounce_number_without_decimal) + " ounce(oz), and after conversion, it's " + str(pound_number_without_decimal) + " pound(lb).")
        print(str(ounce_number_without_decimal) + "(oz) = " + str(pound_number_without_decimal) + "(lb)")
        sleep(1)
        return end_or_repeat_conversion_ounce_to_pound()
    
    elif pound_number_string[find_decimal_point_in_pound+1:] == "0" and ounce_number_input_string[find_decimal_point_in_ounce+1:] != "0":
        pound_number_without_decimal = int(pound_number_string[:find_decimal_point_in_pound])
        print("\nSo, you entered a weight unit: " + str(ounce_number_input) + " ounce(oz), and after conversion, it's " + str(pound_number_without_decimal) + " pound(lb).")
        print(str(ounce_number_input) + "(oz) = " + str(pound_number_without_decimal) + "(lb)")
        sleep(1)
        return end_or_repeat_conversion_ounce_to_pound()
    
    elif pound_number_string[find_decimal_point_in_pound+1:] != "0" and ounce_number_input_string[find_decimal_point_in_ounce+1:] == "0":
        ounce_number_without_decimal = int(ounce_number_input_string[:find_decimal_point_in_ounce])
        print("\nSo, you entered a weight unit: " + str(ounce_number_without_decimal) + " ounce(oz), and after conversion, it's " + str(round(pound_number, 2)) + " pound(lb).")
        print(str(ounce_number_without_decimal) + "(oz) = " + str(round(pound_number, 2)) + "(lb)")
        sleep(1)
        return end_or_repeat_conversion_ounce_to_pound()
    
    else:
        print("\nSo, you entered a weight unit: " + str(ounce_number_input) + " ounce(oz), and after conversion, it's " + str(round(pound_number, 2)) + " pound(lb).")
        print(str(ounce_number_input) + "(oz) = " + str(round(pound_number, 2)) + "(lb)")
        sleep(1)
        return end_or_repeat_conversion_ounce_to_pound()


def end_or_repeat_conversion_ounce_to_pound():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen weight units: Ounce(oz) to Pound(lb), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of weight units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_weight_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_weight_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Ounce(oz) to Pound(lb) program.")
            sleep(1)
            return phase_const.WEIGHT_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Ounce(oz) to Pound(lb) units again.")
            sleep(1)
            return ounce_to_pound()
        else:
            print("\nOut of range, try again!")
            continue
