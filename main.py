import phases_and_constants.phase_constants as phase_const
import phases_and_constants.subphases_constants as subphases_const

from phases_and_constants.intro import intro_print
from phases_and_constants.main_menu import menu_selection
from phases_and_constants.end_program import end_conversion_program

from conversions.temperature_conversion.a_menu_temperature_conversion import temperature_conversion_menu
from conversions.temperature_conversion.fahrenheit_to_celsius import fahrenheit_to_celsius
from conversions.temperature_conversion.celsius_to_fahrenheit import celsius_to_fahrenheit

from conversions.weight_conversion.a_menu_weight_conversion import weight_conversion_menu
from conversions.weight_conversion.ounce_to_gram import ounce_to_gram
from conversions.weight_conversion.gram_to_ounce import gram_to_ounce
from conversions.weight_conversion.pound_to_kilogram import pound_to_kilogram
from conversions.weight_conversion.kilogram_to_pound import kilogram_to_pound
from conversions.weight_conversion.pound_to_ounce import pound_to_ounce
from conversions.weight_conversion.ounce_to_pound import ounce_to_pound
from conversions.weight_conversion.kilogram_to_gram import kilogram_to_gram
from conversions.weight_conversion.gram_to_kilogram import gram_to_kilogram
from conversions.weight_conversion.metric_ton_to_kilogram import metric_ton_to_kilogram
from conversions.weight_conversion.kilogram_to_metric_ton import kilogram_to_metric_ton

from conversions.liquid_conversion.a_menu_liquid_conversion import liquid_conversion_menu
from conversions.liquid_conversion.liters_to_milliliters import liters_to_milliliters
from conversions.liquid_conversion.milliliters_to_liters import milliliters_to_liters
from conversions.liquid_conversion.gallons_to_liters import gallons_to_liters
from conversions.liquid_conversion.liters_to_gallons import liters_to_gallons
from conversions.liquid_conversion.fluid_ounces_to_milliliters import fluid_ounces_to_milliliters
from conversions.liquid_conversion.milliliters_to_fluid_ounces import milliliters_to_fluid_ounces
from conversions.liquid_conversion.cubic_meters_to_liters import cubic_meters_to_liters
from conversions.liquid_conversion.liters_to_cubic_meters import liters_to_cubic_meters
from conversions.liquid_conversion.barrels_to_cubic_meters import barrels_to_cubic_meters
from conversions.liquid_conversion.cubic_meters_to_barrels import cubic_meters_to_barrels

from conversions.dimension_conversion.a_menu_dimension_conversion import dimension_conversion_menu
from conversions.dimension_conversion.meters_to_feet import meters_to_feet
from conversions.dimension_conversion.feet_to_meters import feet_to_meters
from conversions.dimension_conversion.meters_to_inches import meters_to_inches
from conversions.dimension_conversion.inches_to_meters import inches_to_meters
from conversions.dimension_conversion.centimeters_to_inches import centimeters_to_inches
from conversions.dimension_conversion.inches_to_centimeters import inches_to_centimeters
from conversions.dimension_conversion.kilometers_to_miles import kilometers_to_miles
from conversions.dimension_conversion.miles_to_kilometers import miles_to_kilometers
from conversions.dimension_conversion.meters_to_yards import meters_to_yards
from conversions.dimension_conversion.yards_to_meters import yards_to_meters

from conversions.speed_conversion.a_menu_speed_conversion import speed_conversion_menu
from conversions.speed_conversion.kilometers_to_meters_speed import kilometers_to_meters_speed
from conversions.speed_conversion.meters_to_kilometers_speed import meters_to_kilometers_speed
from conversions.speed_conversion.kilometers_to_miles_speed import kilometers_to_miles_speed
from conversions.speed_conversion.miles_to_kilometers_speed import miles_to_kilometers_speed
from conversions.speed_conversion.kilometers_to_knots_speed import kilometers_to_knots_speed
from conversions.speed_conversion.knots_to_kilometers_speed import knots_to_kilometers_speed

from conversions.area_conversion.table_of_area_units import table_of_area_units
from conversions.memory_conversion.table_of_memory_units import table_of_memory_units
from conversions.screen_resolution.table_of_screen_resolutions import table_of_screen_resolutions


# intro of the program, phase --->
intro_print()
current_phase = phase_const.MAIN_MENU_PHASE

while True:
    # main menu phase --->
    if current_phase == phase_const.MAIN_MENU_PHASE:
        current_phase = menu_selection()
        
    # temperature conversion phase --->
    elif current_phase == phase_const.TEMPERATURE_CONVERSION_MENU:
        current_phase = temperature_conversion_menu()
    elif current_phase == subphases_const.FAHRENHEIT_TO_CELSIUS:
        current_phase = fahrenheit_to_celsius()
    elif current_phase == subphases_const.CELSIUS_TO_FAHRENHEIT:
        current_phase = celsius_to_fahrenheit()
    
    # units of weight conversion phase --->
    elif current_phase == phase_const.WEIGHT_CONVERSION_MENU:
        current_phase = weight_conversion_menu()
    elif current_phase == subphases_const.OUNCE_TO_GRAM:
        current_phase = ounce_to_gram()
    elif current_phase == subphases_const.GRAM_TO_OUNCE:
        current_phase = gram_to_ounce()
    elif current_phase == subphases_const.POUND_TO_KILOGRAM:
        current_phase = pound_to_kilogram()
    elif current_phase == subphases_const.KILOGRAM_TO_POUND:
        current_phase = kilogram_to_pound()
    elif current_phase == subphases_const.POUND_TO_OUNCE:
        current_phase = pound_to_ounce()
    elif current_phase == subphases_const.OUNCE_TO_POUND:
        current_phase = ounce_to_pound()
    elif current_phase == subphases_const.KILOGRAM_TO_GRAM:
        current_phase = kilogram_to_gram()
    elif current_phase == subphases_const.GRAM_TO_KILOGRAM:
        current_phase = gram_to_kilogram()
    elif current_phase == subphases_const.METRIC_TON_TO_KILOGRAM:
        current_phase = metric_ton_to_kilogram()
    elif current_phase == subphases_const.KILOGRAM_TO_METRIC_TON:
        current_phase = kilogram_to_metric_ton()
        
    # liquid conversion phase --->    
    elif current_phase == phase_const.LIQUID_CONVERSION_MENU:
        current_phase = liquid_conversion_menu()
    elif current_phase == subphases_const.LITERS_TO_MILLILITERS:
        current_phase = liters_to_milliliters()
    elif current_phase == subphases_const.MILLILITERS_TO_LITERS:
        current_phase = milliliters_to_liters()
    elif current_phase == subphases_const.GALLONS_TO_LITERS:
        current_phase = gallons_to_liters()
    elif current_phase == subphases_const.LITERS_TO_GALLONS:
        current_phase = liters_to_gallons()
    elif current_phase == subphases_const.FLUID_OUNCES_TO_MILLILITERS:
        current_phase = fluid_ounces_to_milliliters()
    elif current_phase == subphases_const.MILLILITERS_TO_FLUID_OUNCES:
        current_phase = milliliters_to_fluid_ounces()
    elif current_phase == subphases_const.CUBIC_METERS_TO_LITERS:
        current_phase = cubic_meters_to_liters()
    elif current_phase == subphases_const.LITERS_TO_CUBIC_METERS:
        current_phase = liters_to_cubic_meters()
    elif current_phase == subphases_const.BARRELS_TO_CUBIC_METERS:
        current_phase = barrels_to_cubic_meters()
    elif current_phase == subphases_const.CUBIC_METERS_TO_BARRELS:
        current_phase = cubic_meters_to_barrels()
    
    # dimension conversion phase --->    
    elif current_phase == phase_const.DIMENSION_CONVERSION_MENU:
        current_phase = dimension_conversion_menu()
    elif current_phase == subphases_const.METERS_TO_FEET:
        current_phase = meters_to_feet()
    elif current_phase == subphases_const.FEET_TO_METERS:
        current_phase = feet_to_meters()
    elif current_phase == subphases_const.METERS_TO_INCHES:
        current_phase = meters_to_inches()
    elif current_phase == subphases_const.INCHES_TO_METERS:
        current_phase = inches_to_meters()
    elif current_phase == subphases_const.CENTIMETERS_TO_INCHES:
        current_phase = centimeters_to_inches()
    elif current_phase == subphases_const.INCHES_TO_CENTIMETERS:
        current_phase = inches_to_centimeters()
    elif current_phase == subphases_const.KILOMETERS_TO_MILES:
        current_phase = kilometers_to_miles()
    elif current_phase == subphases_const.MILES_TO_KILOMETERS:
        current_phase = miles_to_kilometers()
    elif current_phase == subphases_const.METERS_TO_YARDS:
        current_phase = meters_to_yards()
    elif current_phase == subphases_const.YARDS_TO_METERS:
        current_phase = yards_to_meters()
        
    # speed units conversions phase --->
    elif current_phase == phase_const.SPEED_CONVERSION_MENU:
        current_phase = speed_conversion_menu()
    elif current_phase == subphases_const.KILOMETERS_PER_HOUR_TO_METERS_PER_SECOND:
        current_phase = kilometers_to_meters_speed()
    elif current_phase == subphases_const.METERS_PER_SECOND_TO_KILOMETERS_PER_HOUR:
        current_phase = meters_to_kilometers_speed()
    elif current_phase == subphases_const.KILOMETERS_PER_HOUR_TO_MILES_PER_HOUR:
        current_phase = kilometers_to_miles_speed()
    elif current_phase == subphases_const.MILES_PER_HOUR_TO_KILOMETERS_PER_HOUR:
        current_phase = miles_to_kilometers_speed()
    elif current_phase == subphases_const.KILOMETERS_PER_HOUR_TO_KNOTS:
        current_phase = kilometers_to_knots_speed()
    elif current_phase == subphases_const.KNOTS_TO_KILOMETERS_PER_HOUR:
        current_phase = knots_to_kilometers_speed()
    
    # area conversion phase --->    
    elif current_phase == phase_const.AREA_CONVERSION_TABLE:
        current_phase = table_of_area_units()
        
    # memory units and their conversions phase --->
    elif current_phase == phase_const.MEMORY_CONVERSION_TABLE:
        current_phase = table_of_memory_units()
        
    # screen resolutions in pixels phase --->
    elif current_phase == phase_const.SCREEN_RESOLUTIONS_TABLE:
        current_phase = table_of_screen_resolutions()
    
    # end the program phase --->    
    elif current_phase == phase_const.END_CONVERSION_PROGRAM:
        end_conversion_program()
        break
