#The thing can is going to come to our mind is below

# def printdivisor(x):

#     n=1;
#     while(n<=x):
#         if x%n == 0:
#             print(n)
#             n = n+1


# x = int(input("Enter the number"))
# y = printdivisor(x)
# print(y)


#This is the better way, because of the reduced complexity

def printdivisor(x):

    elements = 1 
    while elements*elements <=x:
        if x%elements==0:
            print(elements)

            if(elements !=x//elements ):
                print(x//elements)
        elements = elements +1


x = int(input("enter the number you want to find the divisors for"))
printdivisor(x)






    