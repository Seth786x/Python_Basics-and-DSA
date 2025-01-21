#Some logic I want to clear out before attempting the problem

#one of the basic ways we can reverse a string is by using the slicing in python, which is very convinient 

#let's say the string is :

# stringx = "seth"

# revstringx = stringx[::-1]

# print(revstringx)

##########################

#let's try using other ways 

#we can convert the string into a list, reverse the list and  convert it into a string a again 

stringx = "seth"

listx  = list(stringx)

for i in range(0, len(listx)//2):
    listx[i], listx[len(listx)-1-i] = listx[len(listx)-1-i], listx[i]

stringy = ''.join(listx)

print(stringy)



