"""
"""
import math


def find_speed_in_fwd_and_reverse(vehicle_new_gear_ratio, vehicle_previous_gear_ratio, previous_rpm_in_forward, previous_rpm_in_reverse):
    """
    """
    new_speed_in_forward = (
        (vehicle_new_gear_ratio * previous_rpm_in_forward) / vehicle_previous_gear_ratio)
    new_speed_in_reverse = (
        (vehicle_new_gear_ratio * previous_rpm_in_reverse) / vehicle_previous_gear_ratio)

    return new_speed_in_forward, new_speed_in_reverse


previous_gr = float(input("Enter the previous gear ratio of the vehicle: "))
previous_rpm_in_fwd = float(
    input("Enter the previous RPM in Forward direction: "))
previous_rpm_in_reverse = float(
    input("Enter the previous RPM in Reverse direction: "))
new_gr = float(input("Enter the New gear ratio of the vehicle: "))

new_speed_in_forward, new_speed_in_reverse = find_speed_in_fwd_and_reverse(
    new_gr, previous_gr, previous_rpm_in_fwd, previous_rpm_in_reverse)

print(
    f"The new speed in forward is {math.ceil(new_speed_in_forward)} and new speed in reverse direction is {math.ceil(new_speed_in_reverse)}")
