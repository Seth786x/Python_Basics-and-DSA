

def primecheck(x):
    if x<=1:
        return False
    
    else:
        for i in range(2, int((x**0.5))+1):
            if x%i==0:
                return False
            
    return True 

y = int(input("Enter the number"))
print(primecheck(y))



