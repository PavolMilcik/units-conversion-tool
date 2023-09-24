import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def kilometers_to_knots_speed():
    print("\n\n\tKILOMETERS(km/h) to KNOTS(kn or kt) conversion\n" + SEPARATOR)
    print("You have chosen speed units for conversion, specifically Kilometers per Hour(km/h) units to Knots(kn or kt) units. Let's do it.\n" + SEPARATOR)
    
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
        print("---- Do you want to see the secret formula used to convert Kilometers per Hour(km/h) to Knots(kn or kt)?")
        
        secret_kilometers_to_knots_speed_formula_dict = {"0": "NO and go straight to speed units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_kilometers_to_knots_speed_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Kilometers per Hour(km/h) to Knots(kn or kt) --->\nKnots(kn or kt) = Kilometers per Hour(km/h) * (1/1.852)\n1 kilometer per hour(km/h) is equal to approximately 0.539956803 = 1/1.852 knots(kn or kt).\nUse this formula to convert 20 Kilometers per Hour(km/h) to Knots(kn or kt): 10.8(kn or kt) = 20(km/h) * (1/1.852)\n")
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
        return conversion_kilometers_to_knots_speed(kilometers_number_input)


def conversion_kilometers_to_knots_speed(kilometers_number_input):
    kilometers_number_input_string = str(kilometers_number_input)
    find_decimal_point_in_kilometers = kilometers_number_input_string.find(".")
    
    knots_number = kilometers_number_input * (1/1.852)
    
    knots_number_string = str(knots_number)
    find_decimal_point_in_knots = knots_number_string.find(".")
    
    if knots_number_string[find_decimal_point_in_knots+1:] == "0" and kilometers_number_input_string[find_decimal_point_in_kilometers+1:] == "0":
        knots_number_without_decimal = int(knots_number_string[:find_decimal_point_in_knots])
        kilometers_number_without_decimal = int(kilometers_number_input_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a speed unit: " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h), and after conversion, it's " + str(knots_number_without_decimal) + " knots(kn or kt).")
        print(str(kilometers_number_without_decimal) + "(km/h) = " + str(knots_number_without_decimal) + "(kn or kt)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_knots_speed()
    
    elif knots_number_string[find_decimal_point_in_knots+1:] == "0" and kilometers_number_input_string[find_decimal_point_in_kilometers+1:] != "0":
        knots_number_without_decimal = int(knots_number_string[:find_decimal_point_in_knots])
        print("\nSo, you entered a speed unit: " + str(kilometers_number_input) + " kilometers per hour(km/h), and after conversion, it's " + str(knots_number_without_decimal) + " knots(kn or kt).")
        print(str(kilometers_number_input) + "(km/h) = " + str(knots_number_without_decimal) + "(kn or kt)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_knots_speed()
    
    elif knots_number_string[find_decimal_point_in_knots+1:] != "0" and kilometers_number_input_string[find_decimal_point_in_kilometers+1:] == "0":
        kilometers_number_without_decimal = int(kilometers_number_input_string[:find_decimal_point_in_kilometers])
        print("\nSo, you entered a speed unit: " + str(kilometers_number_without_decimal) + " kilometers per hour(km/h), and after conversion, it's " + str(round(knots_number, 2)) + " knots(kn or kt).")
        print(str(kilometers_number_without_decimal) + "(km/h) = " + str(round(knots_number, 2)) + "(kn or kt)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_knots_speed()
    
    else:
        print("\nSo, you entered a speed unit: " + str(kilometers_number_input) + " kilometers per hour(km/h), and after conversion, it's " + str(round(knots_number, 2)) + " knots(kn or kt).")
        print(str(kilometers_number_input) + "(km/h) = " + str(round(knots_number, 2)) + "(kn or kt)")
        sleep(1)
        return end_or_repeat_conversion_kilometers_to_knots_speed()


def end_or_repeat_conversion_kilometers_to_knots_speed():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen speed units: Kilometers per Hour(km/h) to Knots(kn or kt), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of speed units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_speed_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_speed_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Kilometers per Hour(km/h) to Knots(kn or kt) program.")
            sleep(1)
            return phase_const.SPEED_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Kilometers per Hour(km/h) to Knots(kn or kt) units again.")
            sleep(1)
            return kilometers_to_knots_speed()
        else:
            print("\nOut of range, try again!")
            continue
