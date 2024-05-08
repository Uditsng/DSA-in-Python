import array as pr
myArray = pr.array("i",[2,4,6,8,10])
print('element : ', myArray[3])
def traverseArray(Array):
    for j in Array:  #O(n)
        print(j)     #O(1)

traverseArray(myArray)        
