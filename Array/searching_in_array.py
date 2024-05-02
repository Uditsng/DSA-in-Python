import array as ar

print('Method-1')

myArray = ar.array("i",[1,2,3,4,5,6,7,8,9,10,11])
def linear_search(arr,target):
    for i in range(len(arr)):  #O(n)
        if arr[i]==target:     #O(1)
            return i           #O(1)
    return -1                  #O(1)
    
print("Index :",linear_search(myArray,9))   

print('Method-2')

print('Index :',myArray.index(6))