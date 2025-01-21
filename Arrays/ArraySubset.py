# We have to find whether an array is present in the other or not 

#let's take two arrays at first

def subsetcheck(arr1, arr2):
    setx = set(arr1)
    for i in arr2:
        if i not in setx:
            return False
    return True

print(subsetcheck([7, 8, 6, 5, 5, 5], [7, 8, 6] ))

