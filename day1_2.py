import math

input_path = open("input_d1.txt", "r")
fuel_sum = 0
for mass in input_path:
    fuel_module =math.floor(int(mass)/3) - 2
    fuel_sum += fuel_module

    fuel_for_fuel = 1
    while fuel_for_fuel > 0:
        fuel_for_fuel = math.floor(fuel_module/3) - 2
        if fuel_for_fuel > 0:
            fuel_sum+=fuel_for_fuel
            fuel_module = fuel_for_fuel

print(fuel_sum)
input_path.close()