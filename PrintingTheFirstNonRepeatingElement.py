

# def FirstNR(arr):
#     dictx = {}

#     for i in arr:
#         if i in dictx:
#             dictx[i] += 1

#         else:
#             dictx[i] = 1

#     for i, j in dictx.items():
#         if j==1:
#             return i
            



# print(FirstNR([1, 1, 2, 2, 3, 3, 3 1]))


##########################################

def firsNR(arr):
    dictz = {}

    for i in arr:
        if i in dictz:
            dictz[i] += 1

        else:
            dictz[i] = 1

    for i, j in dictz.items():
        if j ==1:
            return i

    return 0

    listx = [1, 1, 2, 2, 3, 3, 4]
    print(firsNR(listx))
