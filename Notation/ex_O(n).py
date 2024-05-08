
#sampleArray = 5,9,3,0,44,89,64,23,10,55,....

def findBiggestNum(sampleArray):
    biggestNum = sampleArray[0] # O(1)
    for index in range(1,len(sampleArray)): # O(n)
        if sampleArray[index] > biggestNum:  # O(1)
              biggestNum = sampleArray[index]  # O(1)
    print(biggestNum)   # O(1)
                 
'''
adding all time complexities : O(1)+O(n)+O(1)+O(1)+O(1) = O(n)
'''