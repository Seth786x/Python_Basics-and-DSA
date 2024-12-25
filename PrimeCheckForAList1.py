
#This is the most basic way we can check whether a  given number is prime or not, 
#if the number is less than equal to one, then it cannot be a prime number 
#if the number is getting divided by any other number of the range between 2 and the bynber itself, 
#it cannot be a prime number again 

# def primeCheck(x):
#     if x <=1:
#         return False
    
#     i = 2

#     for i in range(2, x):
#         if x%i==0:
#             return False 
        
#     return True 


# print(primeCheck(12))

#let us try to do it with a while loop

# def isprime(x):
#     if x<=1:
#         return False

#     i = 2
#     while i<=x:
#         if x%2==0:return False
       

#     return True

# y = int(input("Enter the number"))
# print(isprime(y))

############################################

#This is more efficient, we only have to go until the root of a number 

# def isprime(x):
#     if x<=1:
#         return False
    
#     i =2
#     while i*i<=x:
#         if x%i==0:
#             return False
#         i = i+1  
        
#     return True

# y = int(input("Enter the number"))
# print(isprime(y))


#To check whether the numbers in a list is integer or not

def isprime(x):
    if x<=1:
        return False

    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
        
    return True

try: 
    
    mapx = map(int, input("Enter the numbers with a space").split())
    listx = list(mapx)

    if listx:
        for i in listx:
            print(isprime(i))

    else:
        print("There are no elements present")



except:
    print("Invalid Input")











