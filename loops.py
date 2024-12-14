#what if you have got to print something a lot of time? I'm sure we won't keep printing the data all the time 
#Here's where loop come into picture

for i in range(0, 20):
    print("I have got to work harder")

#let's give a look at the while loop

pushup = 0
i = 0

while pushup <=30:
    print(" push up number ", i)
    pushup = pushup +1
    i = i+1

#The "range" that we use in for loop has multiple instances of use, look below

lst = list(range(7, 14, 2))
print(lst)

#range is used to generate Numbers: Produces a sequence of numbers within a specified range.

# Parameters:
# range(stop): Generates numbers from 0 to stop-1.
# range(start, stop): Generates numbers from start to stop-1.
# range(start, stop, step): Generates numbers from start to stop-1 with a step increment of step.

#------------------------------------------------------------------------------------------------
#let's run a for loop over the list that we had created earlier above

for i in lst:
    print(i)

#let me print all the elements along with it's position in the list
n = len(lst)
for i in range(n-1, -1, -1):
    print(i, lst[i])

lst1 = [3, 3, 5, 6, 4, 5, 9, 11, 22]
x = 9 
position = -1;

for i in range(len(lst1)):
    if lst1[i] == x:
        position = i
        break

print(position)
