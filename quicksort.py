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

# test = [21, 4, 1]
# print(quicksort(test))

# optimized version
"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    return []

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))