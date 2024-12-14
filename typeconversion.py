x = 1.3
print(int(x))

print(str(x), type(str(x)))

xyz = [1, 2, 3]

print(tuple(xyz), type(tuple(xyz)))

color = ["black", "brown", "grey"]
assignNo = [1, 2 ,3]

#dict(color:assignNo)  !! this isn't how it is supposed to be done

#This is the right way
 
colour = dict(zip(color, assignNo))
print(colour, type(colour))

#next we are converting datatypes into bool

print(bool(), bool({4: "hey"}), bool({4}), bool(""), bool(1))
#the output false means there's no value in the data structure and true if otherwise

#zip is something we'll get to know further