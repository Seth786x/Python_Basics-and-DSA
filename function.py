#A simple add function
def sum3(a, b, c):
    print(a+b+c)

sum3(8, 8, 8)

########################################

lst = [1, 2, 4, 5, 6]

def printlst(lst):
    for i in lst:
        print(i)


printlst(lst)

#----------------------------------------

sum = 0;

for i in lst:
    sum = sum+i
    i = i+1

print(sum)

#----------------------------------------
#let's update the list, add +1 to each element of the list 

print(list(range(len(lst))))

for i in range(len(lst)):
    lst[i]= lst[i] + 1;
    i = i+1;

print(lst)