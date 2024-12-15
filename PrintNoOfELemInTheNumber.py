#A way to count the number of elements in a number 
# x = 1234;

# y = str(x);
# print(len(y));

#let's create a function for the same 
# def countnum(xx):
#     print(len(str(xx)))

# xx = int(input());
# countnum(xx)

#we can also include return instead of printing the value in the function itself

# def countnum(x):
#     return len(str(x));

# x = int(input());
# ans = countnum(x);
# print(ans)



#with simple logic and not using type conversion

def countnum(num):
    count = 0;

    while num>0:
        num=num//10;
        count +=1
    return count;

num = int(input("Enter the number"))
ans = countnum(num)
print(ans)
   