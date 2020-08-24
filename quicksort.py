"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

# O(n2)
# def quicksort(array):
#     low = []
#     high = []
#     equal = []

#     if len(array) <= 1:
#         return array
    
#     for i in array:
#         pivot = array[0]
#         if(i < pivot):
#             low.append(i)
#         elif(i > pivot):
#             high.append(i)
#         else:
#             equal.append(i)

#     return(quicksort(low)+quicksort(equal)+quicksort(high))

# test = [10, 7, 8, 9, 1, 5, 20]
# print(quicksort(test))

# optimized version
# """Implement quick sort in Python.
# Input a list.
# Output a sorted list."""

def quicksort(array):
    pivot_index = 0
    pivot = array[pivot_index]
    store_index = pivot_index + 1

    for x in range(pivot_index, len(array)):
        if array[x] < pivot:
            array[x], array[store_index] = array[store_index], array[x]
    
    pivot = store_index
    store_index = pivot

    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))