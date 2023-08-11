ar = [2,5,8,10,12,20]
ar_search = [1,3,6,9,11,15,23]

def binary_search(ar,n):
    '''
    This method implements binary search on a sorted array
    by ascending order. It will search for the value n in ar, in O(logn) time

    Parameters
    -----------
    ar: array[int]
        An array of integers sorted in ascending order
    n: int
        Integer to search for in the array

    Returns
    -----------
    int, None
        An integer indicating the index where value n is located. Will return
        None when no match is found in the search
    '''
    l = 0
    r = len(ar)-1
    while (l<=r):
        m = (r+l)//2
        if ar[m]<n:
            l = m+1
        elif ar[m]>n:
            r = m - 1
        else:
            return m
    return None

# Test. Will search for each value of ar in ar
for i in ar:
    print(binary_search(ar,i))
