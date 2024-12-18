#Again, first is the most basic code first
# def primecheck(x):
#     for i in range(2,x):
#         if x%i == 0:
#             return False
#     return True

# ans = primecheck(int(input("Enter the number")))
# print(ans)


#and here's a better way to do it 

def isprime(x):
    if x<2:
        return False
    
    i = 2

    while i*i<=x:
        if x%i==0:
            return False
        i = i+1
    
    return True

y = isprime(3)
print(y)


        