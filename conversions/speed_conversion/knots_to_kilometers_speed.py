import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def knots_to_kilometers_speed():
    print("\n\n\tKNOTS(kn or kt) to KILOMETERS(km/h) conversion\n" + SEPARATOR)
    print("You have chosen speed units for conversion, specifically Knots(kn or kt) units to Kilometers per Hour(km/h) units. Let's do it.\n" + SEPARATOR)
    
    sleep(1)
    print("\n\tIntroductory info:")
    print(SEPARATOR)
    print("The knot(kn or kt) is a unit of speed equal to one nautical mile per hour, exactly 1.852 km/h (approximately 1.151 mph or 0.514 m/s).")
    print("1 international knot = 1 nautical mile per hour (by definition).")
    print("The length of the internationally agreed nautical mile is 1852 m.")
    print("Unlike statute - or land based - knots, nautical knots are based directly on the Earth's degree of latitudes.\nOne nautical mile equates exactly to one minute of latitude.")
    print(SEPARATOR + "\n")
    sleep(2)
    
    while True:
        print("---- Do you want to see the secret formula used to convert Knots(kn or kt) to Kilometers per Hour(km/h)?")
        
        secret_knots_to_kilometers_speed_formula_dict = {"0": "NO and go straight to speed units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_knots_to_kilometers_speed_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Knots(kn or kt) to Kilometers per Hour(km/h) --->\nKilometers per Hour(km/h) = Knots(kn or kt) * 1.852\n1 knot(kn or kt) is equal to approximately 1.852 kilometers per hour(km/h).\nUse this formula to convert 15 Knots(kn or kt) to Kilometers per Hour(km/h): 27.78(km/h) = 15(kn or kt) * 1.852\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Knots(kn or kt) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_knots_input = input("Your Knots(kn or kt) value(number) to convert is: ")
        try:
            knots_number_input = float(user_knots_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_knots_to_kilometers_speed(knots_number_input)


def conversion_knots_to_kilometers_speed(knots_number_input):
    knots_number_input_string = str(knots_number_input)
    find_decimal_point_in_knots = knots_number_input_string.find(".")
    
    kilometers_number = knots_number_input * 1.852
    
    kilometers_number_string = str(kilometers_number)
    find_decimal_point_in_kilometers = kilometers_number_string.find(".")
    
    if kilometers_number_string[find_decimal_point_in_kilometers+1:] == "0" and knots_number_input_string[find_decimal_point_in_knots+1:] == "0":
        kilometers_number_without_decimal = int(kilometers_number_string[:find_decimal_point_in_kilometers])
        knots_number_without_decimal = int(knots_number_input_string[:find_decimal_point_in_knots])
        print("\nSo, you entered a speed unit: " + str(knots_number_without_decimal) + " knots(kn or kt), and after conversion, it's " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h).")
        print(str(knots_number_without_decimal) + "(kn or kt) = " + str(kilometers_number_without_decimal) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_knots_to_kilometers_speed()
    
    elif kilometers_number_string[find_decimal_point_in_kilometers+1:] == "0" and knots_number_input_string[find_decimal_point_in_knots+1:] != "0":
        kilometers_number_without_decimal = int(kilometers_number_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a speed unit: " + str(knots_number_input) + " knots(kn or kt), and after conversion, it's " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h).")
        print(str(knots_number_input) + "(kn or kt) = " + str(kilometers_number_without_decimal) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_knots_to_kilometers_speed()
    
    elif kilometers_number_string[find_decimal_point_in_kilometers+1:] != "0" and knots_number_input_string[find_decimal_point_in_knots+1:] == "0":
        knots_number_without_decimal = int(knots_number_input_string[:find_decimal_point_in_knots])
        print("\nSo, you entered a speed unit: " + str(knots_number_without_decimal) + " knots(kn or kt), and after conversion, it's " + str(round(kilometers_number, 2)) + " kilometers per hour(km/h).")
        print(str(knots_number_without_decimal) + "(kn or kt) = " + str(round(kilometers_number, 2)) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_knots_to_kilometers_speed()
    
    else:
        print("\nSo, you entered a speed unit: " + str(knots_number_input) + " knots(kn or kt), and after conversion, it's " + str(round(kilometers_number, 2)) + " kilometers per hour(km/h).")
        print(str(knots_number_input) + "(kn or kt) = " + str(round(kilometers_number, 2)) + "(km/h)")
        sleep(1)
        return end_or_repeat_conversion_knots_to_kilometers_speed()


def end_or_repeat_conversion_knots_to_kilometers_speed():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen speed units: Knots(kn or kt) to Kilometers per Hour(km/h), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of speed units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_speed_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_speed_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Knots(kn or kt) to Kilometers per Hour(km/h) program.")
            sleep(1)
            return phase_const.SPEED_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Knots(kn or kt) to Kilometers per Hour(km/h) units again.")
            sleep(1)
            return knots_to_kilometers_speed()
        else:
            print("\nOut of range, try again!")
            continue
