'''To search if an array contain a number'''

import numpy

myArray = numpy.array([1,2,3,4,5,6,7,8,9,10])

def SearchNum(array,target):
    for i,array[i] in enumerate(array):
        if array[i] == target:
            return "index:",i,"target:",array[i]
    return -1

print(SearchNum(myArray,2))