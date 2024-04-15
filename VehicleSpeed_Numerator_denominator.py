"""
This script converts a decimal float value into its corresponding fraction with 16 bit values. 
"""
import math
from fractions import Fraction


def float_to_fraction(tire_diameter, gr_value):
    """
    Converts the decimal float value into its fraction with 16 bit values.
    """
    decimal_value = (((3 * math.pi)/50) * (16.09344) *
                     ((tire_diameter/1000) / gr_value))
    fraction = Fraction(decimal_value).limit_denominator(2 ** 16 - 1)
    return fraction


get_tire_diameter_value = float(
    input("Enter the diameter of the Tire in millimeters : "))
get_gr_value = float(input("Enter the current Gear ratio of the vehicle : "))

get_fraction = float_to_fraction(get_tire_diameter_value, get_gr_value)
print(
    f"The fraction value for {get_tire_diameter_value} mm and {get_gr_value } GR is {get_fraction}.")
