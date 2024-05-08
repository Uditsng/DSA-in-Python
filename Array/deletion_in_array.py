import array as ar

myArray = ar.array("i",[1,2,3,4,5,6,7,8,9,10,11])
print(myArray)
myArray.remove(2)  #O(n)
print(myArray)

def deletion(arr,target):
    arr.remove(target)
    return arr

print(deletion(myArray,5))    

myArray.pop()
print('After popping : ',myArray)