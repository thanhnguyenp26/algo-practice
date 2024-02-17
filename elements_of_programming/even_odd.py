def even_odd(A):
    '''
    Need to put even numbers in the first portion and odd number in the later portion of 
    the array.
    1 2 3 4 5
    -> 2 4 1 3 5

    TODO:
    Use both ends and swap the numbers
    Two pointers, even = 0 , odd = len(A) - 1
    If A[even] even number, continue and increment even
    If A[even] odd number, A[even] = A[odd] decrease odd 

    TIME COMPLEXITY: O(n)
    SPACE COMPLEXITY: O(1)
    '''
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:

        # even number
        if A[next_even] % 2 == 0:
            next_even += 1

        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A

'''
next_even = 0
next_odd = 2

A[next_even] = 1 -> [3,2,1]
next_even = 0
next_odd = 1

A[0] = 3 -> [2,3,1]
next_even = 1
next_odd = 1

'''
print(even_odd([1,2,3]))
