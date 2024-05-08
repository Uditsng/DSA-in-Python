from mylist_module import myList
print(myList)

''' Searching a element in list '''

#in operator
target = 'udit'  #O(n)

# if target in myList:
#     print(f"{target} is present in list")
# else:
#     print(f"{target} is not present in list")    


#linear search
def linearSearch(list,target):  #O(n)
    for i,value in enumerate(list): #enumerate keep track of target as well as index
        if value == target:
            return i
    return -1

print(linearSearch(myList,target))    