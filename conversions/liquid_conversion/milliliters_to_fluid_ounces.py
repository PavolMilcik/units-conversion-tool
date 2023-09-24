import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def milliliters_to_fluid_ounces():
    print("\n\n\tMILLILITERS(ml) to FLUID OUNCES(US)(fl oz) conversion\n" + SEPARATOR)
    print("You have chosen to convert units of liquid volume, specifically Milliliters(ml) units to Fluid Ounces(fl oz) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Milliliters(ml) to Fluid Ounces(fl oz)?")
        
        secret_milliliters_to_fluid_ounces_formula_dict = {"0": "NO and go straight to liquid units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_milliliters_to_fluid_ounces_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Milliliters(ml) to Fluid Ounces(fl oz) --->\nFluid Ounces(fl oz) = Milliliters(ml) / (1/29.5735)\n1 milliliter(ml) is approximately equal to 0.033814 = 1/29.5735 fluid ounces(US)(fl oz).\nUse this formula to convert 650 milliliters(ml) to fluid ounces(fl oz): 22(fl oz) = 650(ml) * (1/29.5735)\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Milliliters(ml) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_milliliters_input = input("Your Milliliters(ml) value(number) to convert is: ")
        try:
            milliliters_number_input = float(user_milliliters_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_milliliters_to_fluid_ounces(milliliters_number_input)


def conversion_milliliters_to_fluid_ounces(milliliters_number_input):
    milliliters_number_input_string = str(milliliters_number_input)
    find_decimal_point_in_milliliters = milliliters_number_input_string.find(".")
    
    fluid_ounces_number = milliliters_number_input * (1/29.5735)
    
    fluid_ounces_number_string = str(fluid_ounces_number)
    find_decimal_point_in_fluid_ounces = fluid_ounces_number_string.find(".")
    
    if fluid_ounces_number_string[find_decimal_point_in_fluid_ounces+1:] == "0" and milliliters_number_input_string[find_decimal_point_in_milliliters+1:] == "0":
        fluid_ounces_number_without_decimal = int(fluid_ounces_number_string[:find_decimal_point_in_fluid_ounces])
        milliliters_number_without_decimal = int(milliliters_number_input_string[:find_decimal_point_in_milliliters])
        print("\nSo, you entered a liquid unit: " + str(milliliters_number_without_decimal) + " milliliters(ml), and after conversion, it's " + str(fluid_ounces_number_without_decimal) + " fluid_ounces(fl oz).")
        print(str(milliliters_number_without_decimal) + "(ml) = " + str(fluid_ounces_number_without_decimal) + "(fl oz)")
        sleep(1)
        return end_or_repeat_conversion_milliliters_to_fluid_ounces()
    
    elif fluid_ounces_number_string[find_decimal_point_in_fluid_ounces+1:] == "0" and milliliters_number_input_string[find_decimal_point_in_milliliters+1:] != "0":
        fluid_ounces_number_without_decimal = int(fluid_ounces_number_string[:find_decimal_point_in_fluid_ounces])
        print("\nSo, you entered a liquid unit: " + str(milliliters_number_input) + " milliliters(ml), and after conversion, it's " + str(fluid_ounces_number_without_decimal) + " fluid_ounces(fl oz).")
        print(str(milliliters_number_input) + "(ml) = " + str(fluid_ounces_number_without_decimal) + "(fl oz)")
        sleep(1)
        return end_or_repeat_conversion_milliliters_to_fluid_ounces()
    
    elif fluid_ounces_number_string[find_decimal_point_in_fluid_ounces+1:] != "0" and milliliters_number_input_string[find_decimal_point_in_milliliters+1:] == "0":
        milliliters_number_without_decimal = int(milliliters_number_input_string[:find_decimal_point_in_milliliters])
        print("\nSo, you entered a liquid unit: " + str(milliliters_number_without_decimal) + " milliliters(ml), and after conversion, it's " + str(round(fluid_ounces_number, 1)) + " fluid_ounces(fl oz).")
        print(str(milliliters_number_without_decimal) + "(ml) = " + str(round(fluid_ounces_number, 1)) + "(fl oz)")
        sleep(1)
        return end_or_repeat_conversion_milliliters_to_fluid_ounces()
    
    else:
        print("\nSo, you entered a liquid unit: " + str(milliliters_number_input) + " milliliters(ml), and after conversion, it's " + str(round(fluid_ounces_number, 1)) + " fluid_ounces(fl oz).")
        print(str(milliliters_number_input) + "(ml) = " + str(round(fluid_ounces_number, 1)) + "(fl oz)")
        sleep(1)
        return end_or_repeat_conversion_milliliters_to_fluid_ounces()


def end_or_repeat_conversion_milliliters_to_fluid_ounces():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen liquid units: Milliliters(ml) to Fluid Ounces(fl oz), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of liquid units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_liquid_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_liquid_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Milliliters(ml) to Fluid Ounces(fl oz) program.")
            sleep(1)
            return phase_const.LIQUID_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Milliliters(ml) to Fluid Ounces(fl oz) units again.")
            sleep(1)
            return milliliters_to_fluid_ounces()
        else:
            print("\nOut of range, try again!")
            continue
