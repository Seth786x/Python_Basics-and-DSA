# *****
# *****
# *****
# *****
# *****
for i in range(5):
    for i in range(5):
        print("*", end="");
    print();

# *
# **
# ***
# ****
# *****
for i in range(6):
    for j in range(i):
        print("*", end="")
    print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(1, 5):
    for j in range(1, i+1):
        print(j, end=" ")
        i = i+1
    print()  

# 1
# 22
# 333
# 4444
# 55555
for i in range(6):
    for j in range(i):
        print(i, end="")
    print()


# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
n=5
for i in range(n):
    for j in range(1, n-i+1):
        print(j, end = " ")
        
    print()





