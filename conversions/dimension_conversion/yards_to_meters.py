import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def yards_to_meters():
    print("\n\n\tYARDS(yd) to METERS(m) conversion\n" + SEPARATOR)
    print("You have chosen dimension units for conversion, specifically Yards(yd) units to Meters(m) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Yards(yd) to Meters(m)?")
        
        secret_yards_to_meters_formula_dict = {"0": "NO and go straight to dimension units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_yards_to_meters_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Yards(yd) to Meters(m) --->\nMeters(m) = Yards(yd) * (1/1.09361)\n1 yard(yd) is equal to 0.9144 = 1/1.09361 meters(m).\nUse this formula to convert 50 yards(yd) to meters(m): 45.72(m) = 50(yd) * (1/1.09361)\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Yards(yd) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_yards_input = input("Your Yards(yd) value(number) to convert is: ")
        try:
            yards_number_input = float(user_yards_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_yards_to_meters(yards_number_input)


def conversion_yards_to_meters(yards_number_input):
    yards_number_input_string = str(yards_number_input)
    find_decimal_point_in_yards = yards_number_input_string.find(".")
    
    meters_number = yards_number_input * (1/1.09361)
    
    meters_number_string = str(meters_number)
    find_decimal_point_in_meters = meters_number_string.find(".")
    
    if meters_number_string[find_decimal_point_in_meters+1:] == "0" and yards_number_input_string[find_decimal_point_in_yards+1:] == "0":
        meters_number_without_decimal = int(meters_number_string[:find_decimal_point_in_meters])
        yards_number_without_decimal = int(yards_number_input_string[:find_decimal_point_in_yards])
        print("\nSo, you entered a dimension unit: " + str(yards_number_without_decimal) + " yards(yd), and after conversion, it's " + str(meters_number_without_decimal) + " meters(m).")
        print(str(yards_number_without_decimal) + "(yd) = " + str(meters_number_without_decimal) + "(m)")
        sleep(1)
        return end_or_repeat_conversion_yards_to_meters()
    
    elif meters_number_string[find_decimal_point_in_meters+1:] == "0" and yards_number_input_string[find_decimal_point_in_yards+1:] != "0":
        meters_number_without_decimal = int(meters_number_string[:find_decimal_point_in_meters])
        print("\nSo, you entered a dimension unit: " + str(yards_number_input) + " yards(yd), and after conversion, it's " + str(meters_number_without_decimal) + " meters(m).")
        print(str(yards_number_input) + "(yd) = " + str(meters_number_without_decimal) + "(m)")
        sleep(1)
        return end_or_repeat_conversion_yards_to_meters()
    
    elif meters_number_string[find_decimal_point_in_meters+1:] != "0" and yards_number_input_string[find_decimal_point_in_yards+1:] == "0":
        yards_number_without_decimal = int(yards_number_input_string[:find_decimal_point_in_yards])
        print("\nSo, you entered a dimension unit: " + str(yards_number_without_decimal) + " yards(yd), and after conversion, it's " + str(round(meters_number, 2)) + " meters(m).")
        print(str(yards_number_without_decimal) + "(yd) = " + str(round(meters_number, 2)) + "(m)")
        sleep(1)
        return end_or_repeat_conversion_yards_to_meters()
    
    else:
        print("\nSo, you entered a dimension unit: " + str(yards_number_input) + " yards(yd), and after conversion, it's " + str(round(meters_number, 2)) + " meters(m).")
        print(str(yards_number_input) + "(yd) = " + str(round(meters_number, 2)) + "(m)")
        sleep(1)
        return end_or_repeat_conversion_yards_to_meters()


def end_or_repeat_conversion_yards_to_meters():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen dimension units: Yards(yd) to Meters(m), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of dimension units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_dimension_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_dimension_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Yards(yd) to Meters(m) program.")
            sleep(1)
            return phase_const.DIMENSION_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Yards(yd) to Meters(m) units again.")
            sleep(1)
            return yards_to_meters()
        else:
            print("\nOut of range, try again!")
            continue
