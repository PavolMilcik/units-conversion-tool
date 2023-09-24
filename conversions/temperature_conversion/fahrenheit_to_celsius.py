import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def fahrenheit_to_celsius():
    print("\n\n\tFAHRENHEIT(°F) to CELSIUS(°C) conversion\n" + SEPARATOR)
    print("You have chosen to convert temperature from Fahrenheit(°F) to Celsius(°C). Let's do it.\n" + SEPARATOR)
    
    while True:
        print("---- Do you want to see the secret formula used to convert Fahrenheit degrees to Celsius degrees?")
        
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
            print("\nThis is the secret formula used to convert Fahrenheit degrees to Celsius degrees --->\n°C = (°F - 32) * 5/9\nUse this formula to convert 68°F to Celsius: 20°C = (68°F - 32) * 5/9\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Fahrenheit(°F) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_fahrenheit_input = input("Your Fahrenheit(°F) value(number) to convert is: ")
        try:
            fahrenheit_number_input = float(user_fahrenheit_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_fahrenheit_to_celsius(fahrenheit_number_input)
    
    
def conversion_fahrenheit_to_celsius(fahrenheit_number_input):
    fahrenheit_number_input_string = str(fahrenheit_number_input)
    find_decimal_point_in_fahrenheit = fahrenheit_number_input_string.find(".")
    
    celsius_number = (fahrenheit_number_input - 32) * (5/9)
    
    celsius_number_string = str(celsius_number)
    find_decimal_point_in_celsius = celsius_number_string.find(".")
    
    if celsius_number_string[find_decimal_point_in_celsius+1:] == "0" and fahrenheit_number_input_string[find_decimal_point_in_fahrenheit+1:] == "0":
        celsius_number_without_decimal = int(celsius_number_string[:find_decimal_point_in_celsius])
        fahrenheit_number_without_decimal = int(fahrenheit_number_input_string[:find_decimal_point_in_fahrenheit])
        print("\nSo, you entered a temperature of " + str(fahrenheit_number_without_decimal) + " degrees in Fahrenheit(°F), and after conversion, it's " + str(celsius_number_without_decimal) + " degrees Celsius(°C).")
        print(str(fahrenheit_number_without_decimal) + "°F = " + str(celsius_number_without_decimal) + "°C")
        sleep(1)
        return end_or_repeat_conversion_fahrenheit_to_celsius()
    
    elif celsius_number_string[find_decimal_point_in_celsius+1:] == "0" and fahrenheit_number_input_string[find_decimal_point_in_fahrenheit+1:] != "0":
        celsius_number_without_decimal = int(celsius_number_string[:find_decimal_point_in_celsius])
        print("\nSo, you entered a temperature of " + str(fahrenheit_number_input) + " degrees in Fahrenheit(°F), and after conversion, it's " + str(celsius_number_without_decimal) + " degrees Celsius(°C).")
        print(str(fahrenheit_number_input) + "°F = " + str(celsius_number_without_decimal) + "°C")
        sleep(1)
        return end_or_repeat_conversion_fahrenheit_to_celsius()
    
    elif celsius_number_string[find_decimal_point_in_celsius+1:] != "0" and fahrenheit_number_input_string[find_decimal_point_in_fahrenheit+1:] == "0":
        fahrenheit_number_without_decimal = int(fahrenheit_number_input_string[:find_decimal_point_in_fahrenheit])
        print("\nSo, you entered a temperature of " + str(fahrenheit_number_without_decimal) + " degrees in Fahrenheit(°F), and after conversion, it's " + str(round(celsius_number, 1)) + " degrees Celsius(°C).")
        print(str(fahrenheit_number_without_decimal) + "°F = " + str(round(celsius_number, 1)) + "°C")
        sleep(1)
        return end_or_repeat_conversion_fahrenheit_to_celsius()
    
    else:
        print("\nSo, you entered a temperature of " + str(fahrenheit_number_input) + " degrees in Fahrenheit(°F), and after conversion, it's " + str(round(celsius_number, 1)) + " degrees Celsius(°C).")
        print(str(fahrenheit_number_input) + "°F = " + str(round(celsius_number, 1)) + "°C")
        sleep(1)
        return end_or_repeat_conversion_fahrenheit_to_celsius()


def end_or_repeat_conversion_fahrenheit_to_celsius():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion from Fahrenheit(°F) degrees to Celsius(°C) degrees, or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of temperature conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_temperature_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_temperature_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the Fahrenheit(°F) to Celsius(°C) conversion program.")
            sleep(1)
            return phase_const.TEMPERATURE_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Fahrenheit(°F) degrees to Celsius(°C) degrees again.")
            sleep(1)
            return fahrenheit_to_celsius()
        else:
            print("\nOut of range, try again!")
            continue
