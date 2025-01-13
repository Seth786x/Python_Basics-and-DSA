

# def RotateAnArraybyN(arr, n):

#     for i in range(n):
#         first = arr.pop(0)
#         arr.append(first)

#     return arr

# listx = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# print(RotateAnArraybyN(listx, 3))


#the code above will not pass all the test cases because it won't get to all the test cases because of the time complexity, 
#it takes a lot of time 

def rotateAnArraybyd(arr, d):

    n = len(arr)

    temp = arr[:d]

    arr[:n-d] = arr[d:]

    arr[n-d:] = temp

    return arr 

listx = [2, 1, 3, 4, 2]
print(rotateAnArraybyd(listx, 2))

