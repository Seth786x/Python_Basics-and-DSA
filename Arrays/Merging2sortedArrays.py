
#The simplest thing we can do in python is this
# def merge(arr1, arr2):

#     merged = arr1 + arr2
#     ans = sorted(merged)

#     return ans

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 4, 6, 8, 10]

# print(merge(arr1, arr2))

#but the thing we are meant to do while merging lists(arrays) is this
def merge(arr1, arr2):
    merged = []
    i = 0
    j = 0

    while i<len(arr1) and j<len(arr2):

        if arr1[i]<arr2[j]:
            merged.append(arr1[i])
            i = i +1

        else:
            merged.append(arr2[j])
            j = j+1

    while i<len(arr1):
        merged.append(arr1[i])
        i = i+1

    while j<len(arr2):
        merged.append(arr2[j])
        j = j+1

    return merged

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
print(merge(arr1, arr2))

#In python, we can do things a bit simpler
#when handling the remaining elements that are left, we can simply use the extend function to add the elements

# def merge(arr1, arr2):
#     merged = []
#     i = 0
#     j = 0

#     while i<len(arr1) and j<len(arr2):

#         if arr1[i]<arr2[j]:
#             merged.append(arr1[i])
#             i = i +1

#         else:
#             merged.append(arr2[j])
#             j = j+1

#     merged.extend(arr1[i:])
#     merged.extend(arr2[j:])

#     return merged

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 4, 6, 8, 10]
# print(merge(arr1, arr2))

