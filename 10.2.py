__author__ = 'Ayla'


#1. Create a list of numbers in random order.
a=[5,3,1,2,4]
#2. Create a loop that starts at the first element of the list and goes to the second to last element. For each iteration
#in the loop, if the element you are at and the next element are out of order swap them, otherwise leave them alone.
#Print the new list.
for number in a:
        a.sort()
print(a)
#3. What happens if you put the for loop from part 2 inside of another for loop that runs from 1 to the length of the list?

for i in range(1,len(a)):
    for i in a:
        a.sort()
print(a)
