from mylist_module import myList
print(myList)

''' Deletion in list'''

#remove method
myList.remove('udit') #element #O(n)
print(myList)

#pop method
print(myList.pop(4)) #index #O(1) / O(n)
print(myList)

#delete method
del myList[1] #index  #O(n)
print(myList)

del myList[0:2] #using slicing to delete multiple elements
print(myList)