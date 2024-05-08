import numpy

myArray = numpy.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(myArray)

def traversing(array):

    for i in range(len(array)): #for rows
        for j in range(len(array[0])): #for columns
            print(array[i][j])

traversing(myArray)        