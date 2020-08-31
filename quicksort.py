"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

# O(n)
def quicksort(array):
    low = []
    high = []
    equal = []

    if len(array) <= 1:
        return array
    
    for i in array:
        pivot = array[0]
        if(i < pivot):
            low.append(i)
        elif(i > pivot):
            high.append(i)
        else:
            equal.append(i)

    return(quicksort(low)+quicksort(equal)+quicksort(high))

test = [10, 7, 8, 9, 1, 5, 20]
print(quicksort(test))
