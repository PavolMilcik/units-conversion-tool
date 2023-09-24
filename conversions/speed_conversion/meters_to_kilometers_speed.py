import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def meters_to_kilometers_speed():
    print("\n\n\tMETERS(m/s) to KILOMETERS(km/h) conversion\n" + SEPARATOR)
    print("You have chosen speed units for conversion, specifically Meters per Second(m/s) units to Kilometers per Hour(km/h) units. Let's do it.\n" + SEPARATOR)
    
    while True:
        print("---- Do you want to see the secret formula used to convert Meters per Second(m/s) to Kilometers per Hour(km/h)?")
        
        secret_meters_to_kilometers_speed_formula_dict = {"0": "NO and go straight to speed units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_meters_to_kilometers_speed_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Meters per Second(m/s) to Kilometers per Hour(km/h) --->\nKilometers per Hour(km/h) = Meters per Second(m/s) * 3.6\n1 meter per second(m/s) is equal to 3.6 kilometers per hour(km/h).\nUse this formula to convert 2.5 Meters per Second(m/s) to Kilometers per Hour(km/h): 9(km/h) = 2.5(m/s) * 3.6\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Meters per Second(m/s) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_meters_input = input("Your Meters per Second(m/s) value(number) to convert is: ")
        try:
            meters_number_input = float(user_meters_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_meters_to_kilometers_speed(meters_number_input)


def conversion_meters_to_kilometers_speed(meters_number_input):
    meters_number_input_string = str(meters_number_input)
    find_decimal_point_in_meters = meters_number_input_string.find(".")
    
    kilometers_number = meters_number_input * 3.6
    
    kilometers_number_string = str(kilometers_number)
    find_decimal_point_in_kilometers = kilometers_number_string.find(".")
    
    if kilometers_number_string[find_decimal_point_in_kilometers+1:] == "0" and meters_number_input_string[find_decimal_point_in_meters+1:] == "0":
        kilometers_number_without_decimal = int(kilometers_number_string[:find_decimal_point_in_kilometers])
        meters_number_without_decimal = int(meters_number_input_string[:find_decimal_point_in_meters])
        print("\nSo, you entered a speed unit: " + str(meters_number_without_decimal) + " meters per second(m/s), and after conversion, it's " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h).")
        print(str(meters_number_without_decimal) + "(m/s) = " + str(kilometers_number_without_decimal) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_kilometers_speed()
    
    elif kilometers_number_string[find_decimal_point_in_kilometers+1:] == "0" and meters_number_input_string[find_decimal_point_in_meters+1:] != "0":
        kilometers_number_without_decimal = int(kilometers_number_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a speed unit: " + str(meters_number_input) + " meters per second(m/s), and after conversion, it's " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h).")
        print(str(meters_number_input) + "(m/s) = " + str(kilometers_number_without_decimal) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_kilometers_speed()
    
    elif kilometers_number_string[find_decimal_point_in_kilometers+1:] != "0" and meters_number_input_string[find_decimal_point_in_meters+1:] == "0":
        meters_number_without_decimal = int(meters_number_input_string[:find_decimal_point_in_meters])
        print("\nSo, you entered a speed unit: " + str(meters_number_without_decimal) + " meters per second(m/s), and after conversion, it's " + str(round(kilometers_number, 2)) + " kilometers per hour(km/h).")
        print(str(meters_number_without_decimal) + "(m/s) = " + str(round(kilometers_number, 2)) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_kilometers_speed()
    
    else:
        print("\nSo, you entered a speed unit: " + str(meters_number_input) + " meters per second(m/s), and after conversion, it's " + str(round(kilometers_number, 2)) + " kilometers per hour(km/h).")
        print(str(meters_number_input) + "(m/s) = " + str(round(kilometers_number, 2)) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_meters_to_kilometers_speed()


def end_or_repeat_conversion_meters_to_kilometers_speed():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen speed units: Meters per Second(m/s) to Kilometers per Hour(km/h), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of speed units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_speed_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_speed_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Meters per Second(m/s) to Kilometers per Hour(km/h) program.")
            sleep(1)
            return phase_const.SPEED_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Meters per Second(m/s) to Kilometers per Hour(km/h) units again.")
            sleep(1)
            return meters_to_kilometers_speed()
        else:
            print("\nOut of range, try again!")
            continue
