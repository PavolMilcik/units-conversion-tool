import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def kilometers_to_meters_speed():
    print("\n\n\tKILOMETERS(km/h) to METERS(m/s) conversion\n" + SEPARATOR)
    print("You have chosen speed units for conversion, specifically Kilometers per Hour(km/h) units to Meters per Second(m/s) units. Let's do it.\n" + SEPARATOR)
    
    while True:
        print("---- Do you want to see the secret formula used to convert Kilometers per Hour(km/h) to Meters per Second(m/s)?")
        
        secret_kilometers_to_meters_speed_formula_dict = {"0": "NO and go straight to speed units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_kilometers_to_meters_speed_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Kilometers per Hour(km/h) to Meters per Second(m/s) --->\nMeters per Second(m/s) = Kilometers per Hour(km/h) * (1/3.6)\n1 kilometer per hour(km/h) is equal to approximately 0.2777777777777778 = (1/3.6) meters per second(m/s).\nUse this formula to convert 30 Kilometers per Hour(km/h) to Meters per Second(m/s): 8.33(m/s) = 30(km/h) * (1/3.6)\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Kilometers per Hour(km/h) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_kilometers_input = input("Your Kilometers per Hour(km/h) value(number) to convert is: ")
        try:
            kilometers_number_input = float(user_kilometers_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_kilometers_to_meters_speed(kilometers_number_input)


def conversion_kilometers_to_meters_speed(kilometers_number_input):
    kilometers_number_input_string = str(kilometers_number_input)
    find_decimal_point_in_kilometers = kilometers_number_input_string.find(".")
    
    meters_number = kilometers_number_input * (1/3.6)
    
    meters_number_string = str(meters_number)
    find_decimal_point_in_meters = meters_number_string.find(".")
    
    if meters_number_string[find_decimal_point_in_meters+1:] == "0" and kilometers_number_input_string[find_decimal_point_in_kilometers+1:] == "0":
        meters_number_without_decimal = int(meters_number_string[:find_decimal_point_in_meters])
        kilometers_number_without_decimal = int(kilometers_number_input_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a speed unit: " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h), and after conversion, it's " + str(meters_number_without_decimal) + " meters per second(m/s).")
        print(str(kilometers_number_without_decimal) + "(km/h) = " + str(meters_number_without_decimal) + "(m/s)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_meters_speed()
    
    elif meters_number_string[find_decimal_point_in_meters+1:] == "0" and kilometers_number_input_string[find_decimal_point_in_kilometers+1:] != "0":
        meters_number_without_decimal = int(meters_number_string[:find_decimal_point_in_meters])
        print("\nSo, you entered a speed unit: " + str(kilometers_number_input) + " kilometers per hour(km/h), and after conversion, it's " + str(meters_number_without_decimal) + " meters per second(m/s).")
        print(str(kilometers_number_input) + "(km/h) = " + str(meters_number_without_decimal) + "(m/s)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_meters_speed()
    
    elif meters_number_string[find_decimal_point_in_meters+1:] != "0" and kilometers_number_input_string[find_decimal_point_in_kilometers+1:] == "0":
        kilometers_number_without_decimal = int(kilometers_number_input_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a speed unit: " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h), and after conversion, it's " + str(round(meters_number, 2)) + " meters per second(m/s).")
        print(str(kilometers_number_without_decimal) + "(km/h) = " + str(round(meters_number, 2)) + "(m/s)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_meters_speed()
    
    else:
        print("\nSo, you entered a speed unit: " + str(kilometers_number_input) + " kilometers per hour(km/h), and after conversion, it's " + str(round(meters_number, 2)) + " meters per second(m/s).")
        print(str(kilometers_number_input) + "(km/h) = " + str(round(meters_number, 2)) + "(m/s)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_meters_speed()


def end_or_repeat_conversion_kilometers_to_meters_speed():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen speed units: Kilometers per Hour(km/h) to Meters per Second(m/s), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of speed units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_speed_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_speed_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Kilometers per Hour(km/h) to Meters per Second(m/s) program.")
            sleep(1)
            return phase_const.SPEED_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Kilometers per Hour(km/h) to Meters per Second(m/s) units again.")
            sleep(1)
            return kilometers_to_meters_speed()
        else:
            print("\nOut of range, try again!")
            continue
