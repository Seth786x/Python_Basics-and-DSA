
n = int(input(" Enter the number of elements you are going to enter"))

thelist = []

while len(thelist)<n:
    element = str(input("enter the word"))
    thelist.append(element);


for i in range(len(thelist)):
    print(thelist[i], end=" ")

