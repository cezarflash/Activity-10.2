__author__ = 'Ayla'


#1. Create a list of numbers in random order.
a=[1,3,2,4]
#2. Create a loop that starts at the first element of the list and goes to the second to last element. For each iteration
#in the loop, if the element you are at and the next element are out of order swap them, otherwise leave them alone.
#Print the new list.
#for number in a:


for i in range(len(a)-1):
    #a[i]+a[i+1]
    temp=a[1]
    a[1]=a[2]
    a[2]=temp


print(a)

#3. What happens if you put the for loop from part 2 inside of another for loop that runs from 1 to the length of the list?

for j in range(len(a)):
    for number in range(len(a)-1):
        #a[i]+a[i+1]
        temp=a[1]
        a[1]=a[2]
        a[2]=temp
print(a)
