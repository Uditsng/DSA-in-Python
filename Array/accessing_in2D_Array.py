import numpy as np

myArray = np.array( [[1,2,3,4],[5,6,7,8],[10,11,12,13],[11,22,33,44]])

print(myArray)
def accessingElement(Array,rowIndex,columnIndex):
    if rowIndex >= len(Array) or columnIndex >= len(Array[0]):
        print(" Incorrect Index.")
    else:
        print(Array[rowIndex][columnIndex])
print('Accessed Index: ')
accessingElement(myArray,2,1)        