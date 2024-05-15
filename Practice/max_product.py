'''Find the maximum product of two integers in an array where all elements are positive.''' 

#Method 1 (mentor's)
def max_product(arr):
    max1, max2 = 0, 0
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2

'''For each element num, we compare it with max1:

    If num is greater than max1, we update both max1 and max2. max1 becomes num, and max2 becomes the previous value of max1.
    If num is not greater than max1 but is greater than max2, we update only max2 to num.'''

# 1t's method is reliable it does not change real array by sorting and also can handle negative elements 

#Method 2 (Mine)
def max_product(arr):
   arr.sort()
   return arr[len(arr)-1]*(arr[len(arr)-2])

print(max_product([1, 7, 3, 4, 9, 5]))
