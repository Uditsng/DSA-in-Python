import numpy as np

myArray = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])  #O(m,n) ,m = no. of columns, n = no. of rows

# it add at given index of the 2D array
myArray2 = np.insert(myArray, 4 , [10,20,30,40], axis=1) #array, 0,1,2,3(rows),[new elements], axis = 0 (row),axis= 1 (column)
print(myArray2)

print()

# it add at end of the 2D array
myArray3 = np.append(myArray,[[100,200,300,400]],axis=0)
print(myArray3)