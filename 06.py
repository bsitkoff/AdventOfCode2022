from aocd import lines  # like data.splitlines()
import numpy
print(lines)
data = lines.split()
alpha = {}
for val in data:
    if val in alpha:
        print(f'Saw {val} before')
    else:
        print(f'{val} is new/')