"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    pivot = array[0]

    low = []
    high = []
    equal = []
    
    for i in array:
        if(array[i] < pivot):
            low.append(array[i])

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)