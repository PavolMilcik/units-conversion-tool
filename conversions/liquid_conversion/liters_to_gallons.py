import phases_and_constants.phase_constants as phase_const
from phases_and_constants.other_constants import SEPARATOR
from time import sleep


def liters_to_gallons():
    print("\n\n\tLITERS(l) to GALLONS(US)(gal) conversion\n" + SEPARATOR)
    print("You have chosen to convert units of liquid volume, specifically Liters(l) units to Gallons(US)(gal) units. Let's do it.\n" + SEPARATOR)

    while True:
        print("---- Do you want to see the secret formula used to convert Liters(l) to Gallons(US)(gal)?")
        
        secret_liters_to_gallons_formula_dict = {"0": "NO and go straight to liquid units conversion", "1": "YES and show the formula to convert"}
        for k, v in secret_liters_to_gallons_formula_dict.items():
            print(k, " - ", v)
        
        user_input = input("\nYour choice is: ")
        
        if user_input == "0":
            sleep(1)
            print("")
            break
        elif user_input == "1":
            sleep(1)
            print("\nThis is the secret formula used to convert Liters(l) to Gallons(US)(gal) --->\nGallons(US)(gal) = Liters(l) * (1/3.78541)\n1 liter(l) is approximately equal to 0.264172 = 1/3.78541 gallons(US)(gal).\nUse this formula to convert 8 Liters(l) to Gallons(US)(gal): 2.11(US)(gal) = 8(l) * (1/3.78541)\n")
            sleep(2)
            break
        else:
            print("\nOut of range, try again!")
            continue
    
    sleep(1)
    print("---- Please enter the Liters(l) value we are going to convert, just type the number.\nThe number can be whole(integer) or decimal(float).\n")
    
    while True:
        sleep(1)
        user_liters_input = input("Your Liters(l) value(number) to convert is: ")
        try:
            liters_number_input = float(user_liters_input)
        except ValueError:
            print("\nPlease write only integer or float number!\nTry again.\n")
            continue
        sleep(1)
        return conversion_liters_to_gallons(liters_number_input)


def conversion_liters_to_gallons(liters_number_input):
    liters_number_input_string = str(liters_number_input)
    find_decimal_point_in_liters = liters_number_input_string.find(".")
    
    gallons_number = liters_number_input * (1/3.78541)
    
    gallons_number_string = str(gallons_number)
    find_decimal_point_in_gallons = gallons_number_string.find(".")
    
    if gallons_number_string[find_decimal_point_in_gallons+1:] == "0" and liters_number_input_string[find_decimal_point_in_liters+1:] == "0":
        gallons_number_without_decimal = int(gallons_number_string[:find_decimal_point_in_gallons])
        liters_number_without_decimal = int(liters_number_input_string[:find_decimal_point_in_liters])
        print("\nSo, you entered a liquid unit: " + str(liters_number_without_decimal) + " liters(l), and after conversion, it's " + str(gallons_number_without_decimal) + " gallons(US)(gal).")
        print(str(liters_number_without_decimal) + "(l) = " + str(gallons_number_without_decimal) + "(US)(gal)")
        sleep(1)
        return end_or_repeat_conversion_liters_to_gallons()
    
    elif gallons_number_string[find_decimal_point_in_gallons+1:] == "0" and liters_number_input_string[find_decimal_point_in_liters+1:] != "0":
        gallons_number_without_decimal = int(gallons_number_string[:find_decimal_point_in_gallons])
        print("\nSo, you entered a liquid unit: " + str(liters_number_input) + " liters(l), and after conversion, it's " + str(gallons_number_without_decimal) + " gallons(US)(gal).")
        print(str(liters_number_input) + "(l) = " + str(gallons_number_without_decimal) + "(US)(gal)")
        sleep(1)
        return end_or_repeat_conversion_liters_to_gallons()
    
    elif gallons_number_string[find_decimal_point_in_gallons+1:] != "0" and liters_number_input_string[find_decimal_point_in_liters+1:] == "0":
        liters_number_without_decimal = int(liters_number_input_string[:find_decimal_point_in_liters])
        print("\nSo, you entered a liquid unit: " + str(liters_number_without_decimal) + " liters(l), and after conversion, it's " + str(round(gallons_number, 2)) + " gallons(US)(gal).")
        print(str(liters_number_without_decimal) + "(l) = " + str(round(gallons_number, 2)) + "(US)(gal)")
        sleep(1)
        return end_or_repeat_conversion_liters_to_gallons()
    
    else:
        print("\nSo, you entered a liquid unit: " + str(liters_number_input) + " liters(l), and after conversion, it's " + str(round(gallons_number, 2)) + " gallons(US)(gal).")
        print(str(liters_number_input) + "(l) = " + str(round(gallons_number, 2)) + "(US)(gal)")
        sleep(1)
        return end_or_repeat_conversion_liters_to_gallons()


def end_or_repeat_conversion_liters_to_gallons():
    while True:
        sleep(1)
        print("\n---- Do you want to end the conversion of chosen liquid units: Liters(l) to Gallons(US)(gal), or repeat?\nIf you end this type of conversion, you will return to the menu where you can choose another type of liquid units conversion,\nor you can go back to the main menu.")
        
        end_or_repeat_liquid_dict = {"0": "End the current type of conversion", "1": "Repeat this current type of conversion"}
        for k, v in end_or_repeat_liquid_dict.items():
            print(k, " - ", v)
            
        user_input = input("\nYour choice is: ")
        
        if user_input.isdecimal() and user_input == "0":
            sleep(1)
            print("\nI am ending the conversion of Liters(l) to Gallons(US)(gal) program.")
            sleep(1)
            return phase_const.LIQUID_CONVERSION_MENU
        elif user_input.isdecimal() and user_input == "1":
            print("\nAll right then, let's convert Liters(l) to Gallons(US)(gal) units again.")
            sleep(1)
            return liters_to_gallons()
        else:
            print("\nOut of range, try again!")
            continue
