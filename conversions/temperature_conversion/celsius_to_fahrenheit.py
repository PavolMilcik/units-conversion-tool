import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def celsius_to_fahrenheit():
    print("\n\n\tCELSIUS(°C) to FAHRENHEIT(°F) conversion\n" + SEPARATOR)
    print("You have chosen to convert temperature from Celsius(°C) to Fahrenheit(°F). Let's do it.\n" + SEPARATOR)
    
    while True:
        print("---- Do you want to see the secret formula used to convert Celsius degrees to Fahrenheit degrees?")
        
        secret_temperature_formula_dict = {"0": "NO and go straight to temperature conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_temperature_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Celsius degrees to Fahrenheit degrees --->\n°F = (°C * 9/5) + 32\nUse this formula to convert 25°C to Fahrenheit: 77°F = (25°C * 9/5) + 32\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!\n")
            continue
    
    sleep(1)
    print("---- Please enter the Celsius(°C) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_celsius_input = input("Your Celsius(°C) value(number) to convert is: ")
        try:
            celsius_number_input = float(user_celsius_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_celsius_to_fahrenheit(celsius_number_input)
    
    
def conversion_celsius_to_fahrenheit(celsius_number_input):
    celsius_number_input_string = str(celsius_number_input)
    find_decimal_point_in_celsius = celsius_number_input_string.find(".")
    
    fahrenheit_number = (celsius_number_input * (9/5)) + 32

    fahrenheit_number_string = str(fahrenheit_number)
    find_decimal_point_in_fahrenheit = fahrenheit_number_string.find(".")
    
    if fahrenheit_number_string[find_decimal_point_in_fahrenheit+1:] == "0" and celsius_number_input_string[find_decimal_point_in_celsius+1:] == "0":
        fahrenheit_number_without_decimal = int(fahrenheit_number_string[:find_decimal_point_in_fahrenheit])
        celsius_number_without_decimal = int(celsius_number_input_string[:find_decimal_point_in_celsius])
        print("\nSo, you entered a temperature of " + str(celsius_number_without_decimal) + " degrees in Celsius(°C), and after conversion, it's " + str(fahrenheit_number_without_decimal) + " degrees Fahrenheit(°F).")
        print(str(celsius_number_without_decimal) + "°C = " + str(fahrenheit_number_without_decimal) + "°F")
        sleep(1)
        return end_or_repeat_conversion_celsius_to_fahrenheit()
    
    elif fahrenheit_number_string[find_decimal_point_in_fahrenheit+1:] == "0" and celsius_number_input_string[find_decimal_point_in_celsius+1:] != "0":
        fahrenheit_number_without_decimal = int(fahrenheit_number_string[:find_decimal_point_in_fahrenheit])
        print("\nSo, you entered a temperature of " + str(celsius_number_input) + " degrees in Celsius(°C), and after conversion, it's " + str(fahrenheit_number_without_decimal) + " degrees Fahrenheit(°F).")
        print(str(celsius_number_input) + "°C = " + str(fahrenheit_number_without_decimal) + "°F")
        sleep(1)
        return end_or_repeat_conversion_celsius_to_fahrenheit()
    
    elif fahrenheit_number_string[find_decimal_point_in_fahrenheit+1:] != "0" and celsius_number_input_string[find_decimal_point_in_celsius+1:] == "0":
        celsius_number_without_decimal = int(celsius_number_input_string[:find_decimal_point_in_celsius])
        print("\nSo, you entered a temperature of " + str(celsius_number_without_decimal) + " degrees in Celsius(°C), and after conversion, it's " + str(round(fahrenheit_number, 1)) + " degrees Fahrenheit(°F).")
        print(str(celsius_number_without_decimal) + "°C = " + str(round(fahrenheit_number, 1)) + "°F")
        sleep(1)
        return end_or_repeat_conversion_celsius_to_fahrenheit()
    
    else:
        print("\nSo, you entered a temperature of " + str(celsius_number_input) + " degrees in Celsius(°C), and after conversion, it's " + str(round(fahrenheit_number, 1)) + " degrees Fahrenheit(°F).")
        print(str(celsius_number_input) + "°C = " + str(round(fahrenheit_number, 1)) + "°F")
        sleep(1)
        return end_or_repeat_conversion_celsius_to_fahrenheit()


def end_or_repeat_conversion_celsius_to_fahrenheit():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion from Celsius(°C) degrees to Fahrenheit(°F) degrees, or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of temperature conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_temperature_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_temperature_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the Celsius(°C) to Fahrenheit(°F) conversion program.")
            sleep(1)
            return phase_const.TEMPERATURE_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Celsius(°C) degrees to Fahrenheit(°F) degrees again.")
            sleep(1)
            return celsius_to_fahrenheit()
        else:
            print("\nOut of range, try again!")
            continue
