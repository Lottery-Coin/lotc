'''
The purpose of this snippet is to work out the basic logic for the
lottery draw when the time comes to give a block reward. It uses two
lists and a for loop to draw the numbers from the nums list. Only 11
numbers are drawn from the nums list and the 12th number is chosen from
the entry list so that the list has only 1 duplicate number.
'''
from random import choice
from random import shuffle

# List comprehention to populate list with nums 1 to 144
nums = [n for n in range(1, 145, 1)]

# Declare empty list
entry = []

'''
Loop 12 times and randomly choose a number from the nums list.
Shuffle before each choice, then appending choice to entry list.
Removes choice from nums list and checks to see if last interation.
If last interation choose from entry list, sort list and append to list.
'''
for a in range(11):
    shuffle(nums)
    x = choice(nums)
    entry.append(x)
    nums.remove(x)
    if a == 10:
        x = choice(entry)
        entry.sort()
        entry.append(x)
        
print(entry)