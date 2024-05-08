from  mylist_module import myList

print(myList)

''' Insertion at given index'''
myList[3] = 4
 #index method to insert at any given index in list
print(myList)

''' Insertion at any position in list '''
myList.insert(0,10) #O(n)
 #insert method can insert element at any index in list
print(myList)

''' Insertion at end in list '''
myList.append(100) #O(1)
 #append method insert element only at end in list
print(myList)

''' Inserting a list to another list'''
newList = ['x','y','z'] #O(n)
myList.extend(newList)
 #extend method is adding a list of n numbers to existing list 
print(myList)