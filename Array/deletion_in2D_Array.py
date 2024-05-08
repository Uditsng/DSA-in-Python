import numpy

myArray = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(myArray)

myArray2 = numpy.delete(myArray, 1, axis=0) #axis = 0 for row, 1 for column
print(myArray2)