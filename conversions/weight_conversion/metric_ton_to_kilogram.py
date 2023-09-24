import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def metric_ton_to_kilogram():
    print("\n\n\tMETRIC TON(t) to KILOGRAM(kg) conversion\n" + SEPARATOR)
    print("You have chosen weight units for conversion, specifically Metric Ton(t) units to Kilogram(kg) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Metric Ton(t) to Kilogram(kg)?")
        
        secret_metric_ton_to_kilogram_formula_dict = {"0": "NO and go straight to weight units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_metric_ton_to_kilogram_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Metric Ton(t) to Kilogram(kg) --->\nKilograms(kg) = Metric Ton(t) * 1000\n1 metric ton(t) is approximately equal to 1000 kilograms(kg).\nUse this formula to convert 8 metric ton(t) to kilograms(kg): 8000(kg) = 8(t) * 1000\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Metric Ton(t) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_metric_ton_input = input("Your Metric Ton(t) value(number) to convert is: ")
        try:
            metric_ton_number_input = float(user_metric_ton_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_metric_ton_to_kilogram(metric_ton_number_input)


def conversion_metric_ton_to_kilogram(metric_ton_number_input):
    metric_ton_number_input_string = str(metric_ton_number_input)
    find_decimal_point_in_metric_ton = metric_ton_number_input_string.find(".")
    
    kilogram_number = metric_ton_number_input * 1000
    
    kilogram_number_string = str(kilogram_number)
    find_decimal_point_in_kilogram = kilogram_number_string.find(".")
    
    if kilogram_number_string[find_decimal_point_in_kilogram+1:] == "0" and metric_ton_number_input_string[find_decimal_point_in_metric_ton+1:] == "0":
        kilogram_number_without_decimal = int(kilogram_number_string[:find_decimal_point_in_kilogram])
        metric_ton_number_without_decimal = int(metric_ton_number_input_string[:find_decimal_point_in_metric_ton])
        print("\nSo, you entered a weight unit: " + str(metric_ton_number_without_decimal) + " metric_ton(t), and after conversion, it's " + str(kilogram_number_without_decimal) + " kilogram(kg).")
        print(str(metric_ton_number_without_decimal) + "(t) = " + str(kilogram_number_without_decimal) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_metric_ton_to_kilogram()
    
    elif kilogram_number_string[find_decimal_point_in_kilogram+1:] == "0" and metric_ton_number_input_string[find_decimal_point_in_metric_ton+1:] != "0":
        kilogram_number_without_decimal = int(kilogram_number_string[:find_decimal_point_in_kilogram])
        print("\nSo, you entered a weight unit: " + str(metric_ton_number_input) + " metric_ton(t), and after conversion, it's " + str(kilogram_number_without_decimal) + " kilogram(kg).")
        print(str(metric_ton_number_input) + "(t) = " + str(kilogram_number_without_decimal) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_metric_ton_to_kilogram()
    
    elif kilogram_number_string[find_decimal_point_in_kilogram+1:] != "0" and metric_ton_number_input_string[find_decimal_point_in_metric_ton+1:] == "0":
        metric_ton_number_without_decimal = int(metric_ton_number_input_string[:find_decimal_point_in_metric_ton])
        print("\nSo, you entered a weight unit: " + str(metric_ton_number_without_decimal) + " metric_ton(t), and after conversion, it's " + str(round(kilogram_number, 3)) + " kilogram(kg).")
        print(str(metric_ton_number_without_decimal) + "(t) = " + str(round(kilogram_number, 3)) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_metric_ton_to_kilogram()
    
    else:
        print("\nSo, you entered a weight unit: " + str(metric_ton_number_input) + " metric_ton(t), and after conversion, it's " + str(round(kilogram_number, 3)) + " kilogram(kg).")
        print(str(metric_ton_number_input) + "(t) = " + str(round(kilogram_number, 3)) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_metric_ton_to_kilogram()
    
    
def end_or_repeat_conversion_metric_ton_to_kilogram():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen weight units: Metric Ton(t) to Kilogram(kg), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of weight units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_weight_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_weight_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Metric Ton(t) to Kilogram(kg) program.")
            sleep(1)
            return phase_const.WEIGHT_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Metric Ton(t) to Kilogram(kg) units again.")
            sleep(1)
            return metric_ton_to_kilogram()
        else:
            print("\nOut of range, try again!")
            continue
