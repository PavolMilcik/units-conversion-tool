import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def miles_to_kilometers_speed():
    print("\n\n\tMILES(mph) to KILOMETERS(km/h) conversion\n" + SEPARATOR)
    print("You have chosen speed units for conversion, specifically Miles per Hour(mph) units to Kilometers per Hour(km/h) units. Let's do it.\n" + SEPARATOR)
    
    while True:
        print("---- Do you want to see the secret formula used to convert Miles per Hour(mph) to Kilometers per Hour(km/h)?")
        
        secret_miles_to_kilometers_speed_formula_dict = {"0": "NO and go straight to speed units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_miles_to_kilometers_speed_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Miles per Hour(mph) to Kilometers per Hour(km/h) --->\nKilometers per Hour(km/h) = Miles per Hour(mph) * 1.609344\n1 mile per hour(mph) is equal to approximately 1.609344 kilometers per hour(km/h).\nUse this formula to convert 60 Miles per Hour(mph) to Kilometers per Hour(km/h): 96.56(km/h) = 60(mph) * 1.609344\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Miles per Hour(mph) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_miles_input = input("Your Miles per Hour(mph) value(number) to convert is: ")
        try:
            miles_number_input = float(user_miles_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_miles_to_kilometers_speed(miles_number_input)


def conversion_miles_to_kilometers_speed(miles_number_input):
    miles_number_input_string = str(miles_number_input)
    find_decimal_point_in_miles = miles_number_input_string.find(".")
    
    kilometers_number = miles_number_input * 1.609344
    
    kilometers_number_string = str(kilometers_number)
    find_decimal_point_in_kilometers = kilometers_number_string.find(".")
    
    if kilometers_number_string[find_decimal_point_in_kilometers+1:] == "0" and miles_number_input_string[find_decimal_point_in_miles+1:] == "0":
        kilometers_number_without_decimal = int(kilometers_number_string[:find_decimal_point_in_kilometers])
        miles_number_without_decimal = int(miles_number_input_string[:find_decimal_point_in_miles])
        print("\nSo, you entered a speed unit: " + str(miles_number_without_decimal) + " miles per hour(mph), and after conversion, it's " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h).")
        print(str(miles_number_without_decimal) + "(mph) = " + str(kilometers_number_without_decimal) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_miles_to_kilometers_speed()
    
    elif kilometers_number_string[find_decimal_point_in_kilometers+1:] == "0" and miles_number_input_string[find_decimal_point_in_miles+1:] != "0":
        kilometers_number_without_decimal = int(kilometers_number_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a speed unit: " + str(miles_number_input) + " miles per hour(mph), and after conversion, it's " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h).")
        print(str(miles_number_input) + "(mph) = " + str(kilometers_number_without_decimal) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_miles_to_kilometers_speed()
    
    elif kilometers_number_string[find_decimal_point_in_kilometers+1:] != "0" and miles_number_input_string[find_decimal_point_in_miles+1:] == "0":
        miles_number_without_decimal = int(miles_number_input_string[:find_decimal_point_in_miles])
        print("\nSo, you entered a speed unit: " + str(miles_number_without_decimal) + " miles per hour(mph), and after conversion, it's " + str(round(kilometers_number, 2)) + " kilometers per hour(km/h).")
        print(str(miles_number_without_decimal) + "(mph) = " + str(round(kilometers_number, 2)) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_miles_to_kilometers_speed()
    
    else:
        print("\nSo, you entered a speed unit: " + str(miles_number_input) + " miles per hour(mph), and after conversion, it's " + str(round(kilometers_number, 2)) + " kilometers per hour(km/h).")
        print(str(miles_number_input) + "(mph) = " + str(round(kilometers_number, 2)) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_miles_to_kilometers_speed()


def end_or_repeat_conversion_miles_to_kilometers_speed():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen speed units: Miles per Hour(mph) to Kilometers per Hour(km/h), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of speed units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_speed_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_speed_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Miles per Hour(mph) to Kilometers per Hour(km/h) program.")
            sleep(1)
            return phase_const.SPEED_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Miles per Hour(mph) to Kilometers per Hour(km/h) units again.")
            sleep(1)
            return miles_to_kilometers_speed()
        else:
            print("\nOut of range, try again!")
            continue
