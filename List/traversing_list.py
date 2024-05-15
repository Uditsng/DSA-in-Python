''' Traversing List '''
print("\n")

from mylist_module import myList

def traversingList(list):
    for i in list:
        print(i)

traversingList(myList) 

'''Traversing backwards '''
print()

print('Reversed list : ')
for i in reversed(myList):
    print (i)


''' Accessing particular element'''

print('\n','Particular element : ',myList[3])

''' Checking if element is present or not'''
print("\n")

print('udit' in myList) #boolean value 
print('Bhai' in myList)