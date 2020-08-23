"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):

    low = []
    high = []
    equal = []
    
    for i in array:
        pivot = array[0]
        if(array[i] < pivot):
            low.append(array[i])
        elif(array[i] > pivot):
            high.append(array[i])
        else:
            equal.append(array[i])

    # output = ort(low)+sort(equal)+sort(high)
    return(low)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))