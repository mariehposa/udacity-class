def get_fib(position):
    if position == 0 or position == 1:
        return position   #O(1)
    else:
        # print(position - 1, position - 2)
        return(get_fib(position - 1) + get_fib(position - 2)) 
    return -1

# Test cases
print(get_fib(9))