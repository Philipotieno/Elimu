# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]

import math
c = 50
h = 30

value = []

items = [x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2 * c * float(d)/h)))))

print(','.join(value))