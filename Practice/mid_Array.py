
'''Write a function called middle that takes a list and returns 
a new list that contains all but the first and last elements.'''

myList = [1, 2, 3, 4]
s = []
def middle(myList):
    myList.pop()
    s = myList[1::]
    return s
print(middle(myList))    
  

'''or '''

def middles(list):
    return list[1:-1]
print(middles([1,2,3,4]))