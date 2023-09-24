import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def fluid_ounces_to_milliliters():
    print("\n\n\tFLUID OUNCES(US)(fl oz) to MILLILITERS(ml) conversion\n" + SEPARATOR)
    print("You have chosen to convert units of liquid volume, specifically Fluid Ounces(fl oz) units to Milliliters(ml) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Fluid Ounces(fl oz) to Milliliters(ml)?")
        
        secret_fluid_ounces_to_milliliters_formula_dict = {"0": "NO and go straight to liquid units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_fluid_ounces_to_milliliters_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Fluid Ounces(fl oz) to Milliliters(ml) --->\nMilliliters(ml) = Fluid Ounces(fl oz) * 29.5735\n1 fluid ounce(US)(fl oz) = 29.5735 milliliters(ml).\nUse this formula to convert 10 fluid ounces(fl oz) to milliliters(ml): 295.7(ml) = 10(fl oz) * 29.5735\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Fluid Ounces(fl oz) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_fluid_ounces_input = input("Your Fluid Ounces(fl oz) value(number) to convert is: ")
        try:
            fluid_ounces_number_input = float(user_fluid_ounces_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_fluid_ounces_to_milliliters(fluid_ounces_number_input)


def conversion_fluid_ounces_to_milliliters(fluid_ounces_number_input):
    fluid_ounces_number_input_string = str(fluid_ounces_number_input)
    find_decimal_point_in_fluid_ounces = fluid_ounces_number_input_string.find(".")
    
    milliliters_number = fluid_ounces_number_input * 29.5735
    
    milliliters_number_string = str(milliliters_number)
    find_decimal_point_in_milliliters = milliliters_number_string.find(".")
    
    if milliliters_number_string[find_decimal_point_in_milliliters+1:] == "0" and fluid_ounces_number_input_string[find_decimal_point_in_fluid_ounces+1:] == "0":
        milliliters_number_without_decimal = int(milliliters_number_string[:find_decimal_point_in_milliliters])
        fluid_ounces_number_without_decimal = int(fluid_ounces_number_input_string[:find_decimal_point_in_fluid_ounces])
        print("\nSo, you entered a liquid unit: " + str(fluid_ounces_number_without_decimal) + " fluid_ounces(fl oz), and after conversion, it's " + str(milliliters_number_without_decimal) + " milliliters(ml).")
        print(str(fluid_ounces_number_without_decimal) + "(fl oz) = " + str(milliliters_number_without_decimal) + "(ml)")
        sleep(1)
        return end_or_repeat_conversion_fluid_ounces_to_milliliters()
    
    elif milliliters_number_string[find_decimal_point_in_milliliters+1:] == "0" and fluid_ounces_number_input_string[find_decimal_point_in_fluid_ounces+1:] != "0":
        milliliters_number_without_decimal = int(milliliters_number_string[:find_decimal_point_in_milliliters])
        print("\nSo, you entered a liquid unit: " + str(fluid_ounces_number_input) + " fluid_ounces(fl oz), and after conversion, it's " + str(milliliters_number_without_decimal) + " milliliters(ml).")
        print(str(fluid_ounces_number_input) + "(fl oz) = " + str(milliliters_number_without_decimal) + "(ml)")
        sleep(1)
        return end_or_repeat_conversion_fluid_ounces_to_milliliters()
    
    elif milliliters_number_string[find_decimal_point_in_milliliters+1:] != "0" and fluid_ounces_number_input_string[find_decimal_point_in_fluid_ounces+1:] == "0":
        fluid_ounces_number_without_decimal = int(fluid_ounces_number_input_string[:find_decimal_point_in_fluid_ounces])
        print("\nSo, you entered a liquid unit: " + str(fluid_ounces_number_without_decimal) + " fluid_ounces(fl oz), and after conversion, it's " + str(round(milliliters_number, 1)) + " milliliters(ml).")
        print(str(fluid_ounces_number_without_decimal) + "(fl oz) = " + str(round(milliliters_number, 1)) + "(ml)")
        sleep(1)
        return end_or_repeat_conversion_fluid_ounces_to_milliliters()
    
    else:
        print("\nSo, you entered a liquid unit: " + str(fluid_ounces_number_input) + " fluid_ounces(fl oz), and after conversion, it's " + str(round(milliliters_number, 1)) + " milliliters(ml).")
        print(str(fluid_ounces_number_input) + "(fl oz) = " + str(round(milliliters_number, 1)) + "(ml)")
        sleep(1)
        return end_or_repeat_conversion_fluid_ounces_to_milliliters()


def end_or_repeat_conversion_fluid_ounces_to_milliliters():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen liquid units: Fluid Ounces(fl oz) to Milliliters(ml), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of liquid units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_liquid_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_liquid_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Fluid Ounces(fl oz) to Milliliters(ml) program.")
            sleep(1)
            return phase_const.LIQUID_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Fluid Ounces(fl oz) to Milliliters(ml) units again.")
            sleep(1)
            return fluid_ounces_to_milliliters()
        else:
            print("\nOut of range, try again!")
            continue
