import math

input_path = open("input_d1.txt", "r")
fuel_sum = 0
for mass in input_path:
    fuel_sum += math.floor(int(mass)/3) - 2
print(fuel_sum)
input_path.close()