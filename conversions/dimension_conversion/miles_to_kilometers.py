import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def miles_to_kilometers():
    print("\n\n\tMILES(mi) to KILOMETERS(km) conversion\n" + SEPARATOR)
    print("You have chosen dimension units for conversion, specifically Miles(mi) units to Kilometers(km) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Miles(mi) to Kilometers(km)?")
        
        secret_miles_to_kilometers_formula_dict = {"0": "NO and go straight to dimension units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_miles_to_kilometers_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Miles(mi) to Kilometers(km) --->\nKilometers(km) = Miles(mi) * 1.60934\n1 mile(mi) is equal to 1.60934 kilometers(km).\nUse this formula to convert 80 miles(mi) to kilometers(km): 128.747(km) = 80(mi) * 1.60934\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Miles(mi) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_miles_input = input("Your Miles(mi) value(number) to convert is: ")
        try:
            miles_number_input = float(user_miles_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_miles_to_kilometers(miles_number_input)
    
    
def conversion_miles_to_kilometers(miles_number_input):
    miles_number_input_string = str(miles_number_input)
    find_decimal_point_in_miles = miles_number_input_string.find(".")
    
    kilometers_number = miles_number_input * 1.60934
    
    kilometers_number_string = str(kilometers_number)
    find_decimal_point_in_kilometers = kilometers_number_string.find(".")
    
    if kilometers_number_string[find_decimal_point_in_kilometers+1:] == "0" and miles_number_input_string[find_decimal_point_in_miles+1:] == "0":
        kilometers_number_without_decimal = int(kilometers_number_string[:find_decimal_point_in_kilometers])
        miles_number_without_decimal = int(miles_number_input_string[:find_decimal_point_in_miles])
        print("\nSo, you entered a dimension unit: " + str(miles_number_without_decimal) + " miles(mi), and after conversion, it's " + str(kilometers_number_without_decimal) + " kilometers(km).")
        print(str(miles_number_without_decimal) + "(mi) = " + str(kilometers_number_without_decimal) + "(km)")
        sleep(1)
        return end_or_repeat_conversion_miles_to_kilometers()
    
    elif kilometers_number_string[find_decimal_point_in_kilometers+1:] == "0" and miles_number_input_string[find_decimal_point_in_miles+1:] != "0":
        kilometers_number_without_decimal = int(kilometers_number_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a dimension unit: " + str(miles_number_input) + " miles(mi), and after conversion, it's " + str(kilometers_number_without_decimal) + " kilometers(km).")
        print(str(miles_number_input) + "(mi) = " + str(kilometers_number_without_decimal) + "(km)")
        sleep(1)
        return end_or_repeat_conversion_miles_to_kilometers()
    
    elif kilometers_number_string[find_decimal_point_in_kilometers+1:] != "0" and miles_number_input_string[find_decimal_point_in_miles+1:] == "0":
        miles_number_without_decimal = int(miles_number_input_string[:find_decimal_point_in_miles])
        print("\nSo, you entered a dimension unit: " + str(miles_number_without_decimal) + " miles(mi), and after conversion, it's " + str(round(kilometers_number, 3)) + " kilometers(km).")
        print(str(miles_number_without_decimal) + "(mi) = " + str(round(kilometers_number, 3)) + "(km)")
        sleep(1)
        return end_or_repeat_conversion_miles_to_kilometers()
    
    else:
        print("\nSo, you entered a dimension unit: " + str(miles_number_input) + " miles(mi), and after conversion, it's " + str(round(kilometers_number, 3)) + " kilometers(km).")
        print(str(miles_number_input) + "(mi) = " + str(round(kilometers_number, 3)) + "(km)")
        sleep(1)
        return end_or_repeat_conversion_miles_to_kilometers()


def end_or_repeat_conversion_miles_to_kilometers():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen dimension units: Miles(mi) to Kilometers(km), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of dimension units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_dimension_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_dimension_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Miles(mi) to Kilometers(km) program.")
            sleep(1)
            return phase_const.DIMENSION_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Miles(mi) to Kilometers(km) units again.")
            sleep(1)
            return miles_to_kilometers()
        else:
            print("\nOut of range, try again!")
            continue
