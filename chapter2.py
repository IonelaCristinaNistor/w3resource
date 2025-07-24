import math

# width = 17
# height = 12.0
# delimiter = '.'
#
# print(width / 2)
# print(width / 2.0)
# print(height / 3)
# print(1 + 2 * 5)
# print(delimiter * 5)

# r = 5
# volume = (4/3) * math.pi * (r ** 3)
# print(f"Volume of the sphere: {volume:.2f}") # cu doua zecimale

price = 24.95
#discount = 40 / 100
shipping_cost = 3
shipping_cost_additional = 0.75

total = ((price * (40/100) + shipping_cost) * 60) + shipping_cost_additional * 60
print(total)