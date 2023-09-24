import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def ounce_to_gram():
    print("\n\n\tOUNCE(oz) to GRAM(g) conversion\n" + SEPARATOR)
    print("You have chosen weight units for conversion, specifically Ounce(oz) units to Gram(g) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Ounce(oz) to Gram(g)?")
        
        secret_ounce_to_gram_formula_dict = {"0": "NO and go straight to weight units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_ounce_to_gram_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Ounce(oz) to Gram(g) --->\nGrams(g) = Ounce(oz) * 28.34952\n1 ounce(oz) is approximately equal to 28.34952 grams(g).\nUse this formula to convert 5 ounce(oz) to grams(g): 141.7476(g) = 5(oz) * 28.34952\n")
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
        return conversion_ounce_to_gram(ounce_number_input)


def conversion_ounce_to_gram(ounce_number_input):
    ounce_number_input_string = str(ounce_number_input)
    find_decimal_point_in_ounce = ounce_number_input_string.find(".")
    
    gram_number = ounce_number_input * 28.34952
    
    gram_number_string = str(gram_number)
    find_decimal_point_in_gram = gram_number_string.find(".")
    
    if gram_number_string[find_decimal_point_in_gram+1:] == "0" and ounce_number_input_string[find_decimal_point_in_ounce+1:] == "0":
        gram_number_without_decimal = int(gram_number_string[:find_decimal_point_in_gram])
        ounce_number_without_decimal = int(ounce_number_input_string[:find_decimal_point_in_ounce])
        print("\nSo, you entered a weight unit: " + str(ounce_number_without_decimal) + " ounce(oz), and after conversion, it's " + str(gram_number_without_decimal) + " gram(g).")
        print(str(ounce_number_without_decimal) + "(oz) = " + str(gram_number_without_decimal) + "(g)")
        sleep(1)
        return end_or_repeat_conversion_ounce_to_gram()
    
    elif gram_number_string[find_decimal_point_in_gram+1:] == "0" and ounce_number_input_string[find_decimal_point_in_ounce+1:] != "0":
        gram_number_without_decimal = int(gram_number_string[:find_decimal_point_in_gram])
        print("\nSo, you entered a weight unit: " + str(ounce_number_input) + " ounce(oz), and after conversion, it's " + str(gram_number_without_decimal) + " gram(g).")
        print(str(ounce_number_input) + "(oz) = " + str(gram_number_without_decimal) + "(g)")
        sleep(1)
        return end_or_repeat_conversion_ounce_to_gram()
    
    elif gram_number_string[find_decimal_point_in_gram+1:] != "0" and ounce_number_input_string[find_decimal_point_in_ounce+1:] == "0":
        ounce_number_without_decimal = int(ounce_number_input_string[:find_decimal_point_in_ounce])
        print("\nSo, you entered a weight unit: " + str(ounce_number_without_decimal) + " ounce(oz), and after conversion, it's " + str(round(gram_number, 2)) + " gram(g).")
        print(str(ounce_number_without_decimal) + "(oz) = " + str(round(gram_number, 2)) + "(g)")
        sleep(1)
        return end_or_repeat_conversion_ounce_to_gram()
    
    else:
        print("\nSo, you entered a weight unit: " + str(ounce_number_input) + " ounce(oz), and after conversion, it's " + str(round(gram_number, 2)) + " gram(g).")
        print(str(ounce_number_input) + "(oz) = " + str(round(gram_number, 2)) + "(g)")
        sleep(1)
        return end_or_repeat_conversion_ounce_to_gram()
    
    
def end_or_repeat_conversion_ounce_to_gram():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen weight units: Ounce(oz) to Gram(g), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of weight units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_weight_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_weight_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Ounce(oz) to Gram(g) program.")
            sleep(1)
            return phase_const.WEIGHT_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Ounce(oz) to Gram(g) units again.")
            sleep(1)
            return ounce_to_gram()
        else:
            print("\nOut of range, try again!")
            continue
