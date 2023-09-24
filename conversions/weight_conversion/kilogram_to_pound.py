import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def kilogram_to_pound():
    print("\n\n\tKILOGRAM(kg) to POUND(lb) conversion\n" + SEPARATOR)
    print("You have chosen weight units for conversion, specifically Kilogram(kg) units to Pound(lb) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Kilogram(kg) to Pound(lb)?")
        
        secret_kilogram_to_pound_formula_dict = {"0": "NO and go straight to weight units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_kilogram_to_pound_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Kilogram(kg) to Pound(lb) --->\nPound(lb) = Kilogram(kg) * 0.453592\n1 kilogram(kg) is approximately equal to 2.20462 pounds(lb).\nUse this formula to convert 59 kilograms(kg) to pounds(lb): 130.1(lb) = 59(kg) * 2.20462\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Kilogram(kg) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_kilogram_input = input("Your Kilogram(kg) value(number) to convert is: ")
        try:
            kilogram_number_input = float(user_kilogram_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_kilogram_to_pound(kilogram_number_input)
    

def conversion_kilogram_to_pound(kilogram_number_input):
    kilogram_number_input_string = str(kilogram_number_input)
    find_decimal_point_in_kilogram = kilogram_number_input_string.find(".")
    
    pound_number = kilogram_number_input * 2.20462
    
    pound_number_string = str(pound_number)
    find_decimal_point_in_pound = pound_number_string.find(".")
    
    if pound_number_string[find_decimal_point_in_pound+1:] == "0" and kilogram_number_input_string[find_decimal_point_in_kilogram+1:] == "0":
        pound_number_without_decimal = int(pound_number_string[:find_decimal_point_in_pound])
        kilogram_number_without_decimal = int(kilogram_number_input_string[:find_decimal_point_in_kilogram])
        print("\nSo, you entered a weight unit: " + str(kilogram_number_without_decimal) + " kilogram(kg), and after conversion, it's " + str(pound_number_without_decimal) + " pound(lb).")
        print(str(kilogram_number_without_decimal) + "(kg) = " + str(pound_number_without_decimal) + "(lb)")
        sleep(1)
        return end_or_repeat_conversion_kilogram_to_pound()
    
    elif pound_number_string[find_decimal_point_in_pound+1:] == "0" and kilogram_number_input_string[find_decimal_point_in_kilogram+1:] != "0":
        pound_number_without_decimal = int(pound_number_string[:find_decimal_point_in_pound])
        print("\nSo, you entered a weight unit: " + str(kilogram_number_input) + " kilogram(kg), and after conversion, it's " + str(pound_number_without_decimal) + " pound(lb).")
        print(str(kilogram_number_input) + "(kg) = " + str(pound_number_without_decimal) + "(lb)")
        sleep(1)
        return end_or_repeat_conversion_kilogram_to_pound()
    
    elif pound_number_string[find_decimal_point_in_pound+1:] != "0" and kilogram_number_input_string[find_decimal_point_in_kilogram+1:] == "0":
        kilogram_number_without_decimal = int(kilogram_number_input_string[:find_decimal_point_in_kilogram])
        print("\nSo, you entered a weight unit: " + str(kilogram_number_without_decimal) + " kilogram(kg), and after conversion, it's " + str(round(pound_number, 1)) + " pound(lb).")
        print(str(kilogram_number_without_decimal) + "(kg) = " + str(round(pound_number, 1)) + "(lb)")
        sleep(1)
        return end_or_repeat_conversion_kilogram_to_pound()
    
    else:
        print("\nSo, you entered a weight unit: " + str(kilogram_number_input) + " kilogram(kg), and after conversion, it's " + str(round(pound_number, 1)) + " pound(lb).")
        print(str(kilogram_number_input) + "(kg) = " + str(round(pound_number, 1)) + "(lb)")
        sleep(1)
        return end_or_repeat_conversion_kilogram_to_pound()
    
    
def end_or_repeat_conversion_kilogram_to_pound():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen weight units: Kilogram(kg) to Pound(lb), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of weight units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_weight_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_weight_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Kilogram(kg) to Pound(lb) program.")
            sleep(1)
            return phase_const.WEIGHT_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Kilogram(kg) to Pound(lb) units again.")
            sleep(1)
            return kilogram_to_pound()
        else:
            print("\nOut of range, try again!")
            continue
    