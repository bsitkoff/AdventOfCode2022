import numpy as np
from aocd import lines  # like data.splitlines()
def get_value(letter):
    if letter.isupper():
        v = (ord(letter)-38)
#        print(f'The value of {letter} is {v}')
    else:
        v = (ord(letter) - 96)
#        print(f'The value of {letter} is {v}')
    return(v)
#Part 1
sum = 0
for l in lines:
    size = len(l)
    left = l[0:size//2]
    right = l[size//2:size]
#    print(f'Full string has {size} chars: {l}. Left: {left}, Right: {right}')
    for char in left:
        if char in right:
#            print(f'Both sides contain: {char}')
            d = char
    sum += get_value(d)
print(f'The part 1 total sum is: {sum}')
#Part 2
sum = 0
for l in range(0,len(lines),3):
    one = lines[l]
    two = lines[l+1]
    three = lines[l+2]
    for char in one:
        if char in two and char in three:
            val = get_value(char)
            sum += val
            print(f'There are three occurrences of {char} in {lines[l:l+3]}, adding {val} to {sum}.')
            break
print(sum)