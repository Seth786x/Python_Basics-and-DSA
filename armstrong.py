def armstrong(x):

    power = len(str(x))
    numbers = 0
    arms = 0
    while(x>0):
        digit = x%10
        arms = arms + digit**power
        x = x//10

    return arms

x = int(input("Enter the integer that you want to calculate the armstrong of"))
y = armstrong(x)
print(y)

