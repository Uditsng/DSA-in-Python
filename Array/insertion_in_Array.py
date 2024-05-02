import array as ar
myArray = ar.array("i", [1,2,3,4,5,6,7])  #O(n)
myArray.insert(0,5)  #it can add element at any given position 
print(myArray)

myArray.append(101)  #it add element at end of array
print(myArray)  

myArray2 = ar.array("i",[9,8,7,6,5,4,3])
myArray.extend(myArray2)    #it insert an array to another and extend the array
print(myArray)

myList =  [77,99,55,22,56,]
myArray.fromlist(myList)
print("list + array :",myArray)