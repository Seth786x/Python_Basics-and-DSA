name = "seth"

print(name[0])
print(name[1])
print(name[2])
print(name[3])

print("------------------")
for i in name:
    print(i)

print("------------------")

print(name[0:3])
print(name[0:4])

#You maybe wondering why the 3rd position wasn't included, that's because the last limit isn't given as a output

#We can also print with intervals, like this
print(name[0:4:2])

#let's try to print the string in reverse
print(name[-1::-1])
#The first -1 indicates the last elements, the second part is left blank because it has to go till the end of the string, and at last the -1 traverses the string in a backward fashion 

#we can traverse the same way in other data structures, let's look at a string

lst = [36, "seth", "77x", 36]
print(lst[0::2])
print(lst[-1::-1])

#let's say we intend to change a string, my full name is seth ken
#let's try adding it 

fullname = name[0:4] + " ken"
print(fullname)

#now, imagine if we have a string which has multiple elements in it separated by space
#we can split each on of them using the split() function

sentence = "I have always tried to be stronger than my weak half"
print(sentence.split())

#we can also convert a list into a string
lstx = ["the ", "one", "stoic"]
str = "|".join(lstx)
print(str, type(str))