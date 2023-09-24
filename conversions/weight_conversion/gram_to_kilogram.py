import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def gram_to_kilogram():
    print("\n\n\tGRAM(g) to KILOGRAM(kg) conversion\n" + SEPARATOR)
    print("You have chosen weight units for conversion, specifically Gram(g) units to Kilogram(kg) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Gram(g) to Kilogram(kg)?")
        
        secret_gram_to_kilogram_formula_dict = {"0": "NO and go straight to weight units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_gram_to_kilogram_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Gram(g) to Kilogram(kg) --->\nKilograms(kg) = Grams(g) / 1000\n1 grams(g) is approximately equal to 1/1000 or 0.001 kilograms(kg).\nUse this formula to convert 2830 grams(g) to kilograms(kg): 2.83(kg) = 2830(g) / 1000\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Gram(g) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_gram_input = input("Your Gram(g) value(number) to convert is: ")
        try:
            gram_number_input = float(user_gram_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_gram_to_kilogram(gram_number_input)
    

def conversion_gram_to_kilogram(gram_number_input):
    gram_number_input_string = str(gram_number_input)
    find_decimal_point_in_gram = gram_number_input_string.find(".")
    
    kilogram_number = gram_number_input / 1000
    
    kilogram_number_string = str(kilogram_number)
    find_decimal_point_in_kilogram = kilogram_number_string.find(".")
    
    if kilogram_number_string[find_decimal_point_in_kilogram+1:] == "0" and gram_number_input_string[find_decimal_point_in_gram+1:] == "0":
        kilogram_number_without_decimal = int(kilogram_number_string[:find_decimal_point_in_kilogram])
        gram_number_without_decimal = int(gram_number_input_string[:find_decimal_point_in_gram])
        print("\nSo, you entered a weight unit: " + str(gram_number_without_decimal) + " gram(g), and after conversion, it's " + str(kilogram_number_without_decimal) + " kilogram(kg).")
        print(str(gram_number_without_decimal) + "(g) = " + str(kilogram_number_without_decimal) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_gram_to_kilogram()
    
    elif kilogram_number_string[find_decimal_point_in_kilogram+1:] == "0" and gram_number_input_string[find_decimal_point_in_gram+1:] != "0":
        kilogram_number_without_decimal = int(kilogram_number_string[:find_decimal_point_in_kilogram])
        print("\nSo, you entered a weight unit: " + str(gram_number_input) + " gram(g), and after conversion, it's " + str(kilogram_number_without_decimal) + " kilogram(kg).")
        print(str(gram_number_input) + "(g) = " + str(kilogram_number_without_decimal) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_gram_to_kilogram()
    
    elif kilogram_number_string[find_decimal_point_in_kilogram+1:] != "0" and gram_number_input_string[find_decimal_point_in_gram+1:] == "0":
        gram_number_without_decimal = int(gram_number_input_string[:find_decimal_point_in_gram])
        print("\nSo, you entered a weight unit: " + str(gram_number_without_decimal) + " gram(g), and after conversion, it's " + str(round(kilogram_number, 3)) + " kilogram(kg).")
        print(str(gram_number_without_decimal) + "(g) = " + str(round(kilogram_number, 3)) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_gram_to_kilogram()
    
    else:
        print("\nSo, you entered a weight unit: " + str(gram_number_input) + " gram(g), and after conversion, it's " + str(round(kilogram_number, 3)) + " kilogram(kg).")
        print(str(gram_number_input) + "(g) = " + str(round(kilogram_number, 3)) + "(kg)")
        sleep(1)
        return end_or_repeat_conversion_gram_to_kilogram()
    

    
def end_or_repeat_conversion_gram_to_kilogram():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen weight units: Gram(g) to Kilogram(kg), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of weight units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_weight_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_weight_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Gram(g) to Kilogram(kg) program.")
            sleep(1)
            return phase_const.WEIGHT_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Gram(g) to Kilogram(kg) units again.")
            sleep(1)
            return gram_to_kilogram()
        else:
            print("\nOut of range, try again!")
            continue
    