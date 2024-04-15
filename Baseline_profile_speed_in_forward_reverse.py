import math

def find_speed_in_fwd_and_reverse(vehicle_new_gear_ratio, vehicle_previous_gear_ratio, previous_rpm_in_forward, previous_rpm_in_reverse):
    """
    Calculate the new speed in both forward and reverse directions after changing the gear ratio.

    Parameters:
        vehicle_new_gear_ratio (float): The new gear ratio of the vehicle.
        vehicle_previous_gear_ratio (float): The previous gear ratio of the vehicle.
        previous_rpm_in_forward (float): The previous RPM (Revolutions Per Minute) in forward direction.
        previous_rpm_in_reverse (float): The previous RPM (Revolutions Per Minute) in reverse direction.

    Returns:
        tuple: A tuple containing two elements:
            - The new speed in forward direction (float).
            - The new speed in reverse direction (float).
    """
    new_speed_in_forward = (vehicle_new_gear_ratio * previous_rpm_in_forward) / vehicle_previous_gear_ratio
    new_speed_in_reverse = (vehicle_new_gear_ratio * previous_rpm_in_reverse) / vehicle_previous_gear_ratio

    return new_speed_in_forward, new_speed_in_reverse

# Get input from the user
previous_gr = float(input("Enter the previous gear ratio of the vehicle: "))
previous_rpm_in_fwd = float(input("Enter the previous RPM in Forward direction: "))
previous_rpm_in_reverse = float(input("Enter the previous RPM in Reverse direction: "))
new_gr = float(input("Enter the New gear ratio of the vehicle: "))

# Calculate new speeds
new_speed_in_forward, new_speed_in_reverse = find_speed_in_fwd_and_reverse(new_gr, previous_gr, previous_rpm_in_fwd, previous_rpm_in_reverse)

# Print the results
print(f"The new speed in forward is {math.ceil(new_speed_in_forward)} and new speed in reverse direction is {math.ceil(new_speed_in_reverse)}")
