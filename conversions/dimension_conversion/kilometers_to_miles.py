import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def kilometers_to_miles():
    print("\n\n\tKILOMETERS(km) to MILES(mi) conversion\n" + SEPARATOR)
    print("You have chosen dimension units for conversion, specifically Kilometers(km) units to Miles(mi) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Kilometers(km) to Miles(mi)?")
        
        secret_kilometers_to_miles_formula_dict = {"0": "NO and go straight to dimension units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_kilometers_to_miles_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Kilometers(km) to Miles(mi) --->\nMiles(mi) = Kilometers(km) * (1/1.60934)\n1 kilometer(km) is equal to 0.621371 = 1/1.60934 miles(mi).\nUse this formula to convert 50 kilometers(km) to miles(mi): 31.069(mi) = 50(km) * (1/1.60934)\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Kilometers(km) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_kilometers_input = input("Your Kilometers(km) value(number) to convert is: ")
        try:
            kilometers_number_input = float(user_kilometers_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_kilometers_to_miles(kilometers_number_input)


def conversion_kilometers_to_miles(kilometers_number_input):
    kilometers_number_input_string = str(kilometers_number_input)
    find_decimal_point_in_kilometers = kilometers_number_input_string.find(".")
    
    miles_number = kilometers_number_input * (1/1.60934)
    
    miles_number_string = str(miles_number)
    find_decimal_point_in_miles = miles_number_string.find(".")
    
    if miles_number_string[find_decimal_point_in_miles+1:] == "0" and kilometers_number_input_string[find_decimal_point_in_kilometers+1:] == "0":
        miles_number_without_decimal = int(miles_number_string[:find_decimal_point_in_miles])
        kilometers_number_without_decimal = int(kilometers_number_input_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a dimension unit: " + str(kilometers_number_without_decimal) + " kilometers(km), and after conversion, it's " + str(miles_number_without_decimal) + " miles(mi).")
        print(str(kilometers_number_without_decimal) + "(km) = " + str(miles_number_without_decimal) + "(mi)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_miles()
    
    elif miles_number_string[find_decimal_point_in_miles+1:] == "0" and kilometers_number_input_string[find_decimal_point_in_kilometers+1:] != "0":
        miles_number_without_decimal = int(miles_number_string[:find_decimal_point_in_miles])
        print("\nSo, you entered a dimension unit: " + str(kilometers_number_input) + " kilometers(km), and after conversion, it's " + str(miles_number_without_decimal) + " miles(mi).")
        print(str(kilometers_number_input) + "(km) = " + str(miles_number_without_decimal) + "(mi)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_miles()
    
    elif miles_number_string[find_decimal_point_in_miles+1:] != "0" and kilometers_number_input_string[find_decimal_point_in_kilometers+1:] == "0":
        kilometers_number_without_decimal = int(kilometers_number_input_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a dimension unit: " + str(kilometers_number_without_decimal) + " kilometers(km), and after conversion, it's " + str(round(miles_number, 3)) + " miles(mi).")
        print(str(kilometers_number_without_decimal) + "(km) = " + str(round(miles_number, 3)) + "(mi)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_miles()
    
    else:
        print("\nSo, you entered a dimension unit: " + str(kilometers_number_input) + " kilometers(km), and after conversion, it's " + str(round(miles_number, 3)) + " miles(mi).")
        print(str(kilometers_number_input) + "(km) = " + str(round(miles_number, 3)) + "(mi)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_miles()


def end_or_repeat_conversion_kilometers_to_miles():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen dimension units: Kilometers(km) to Miles(mi), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of dimension units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_dimension_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_dimension_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Kilometers(km) to Miles(mi) program.")
            sleep(1)
            return phase_const.DIMENSION_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Kilometers(km) to Miles(mi) units again.")
            sleep(1)
            return kilometers_to_miles()
        else:
            print("\nOut of range, try again!")
            continue
