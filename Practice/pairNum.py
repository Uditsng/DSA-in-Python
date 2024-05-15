''' Find pairs or Two sum'''
def findPair(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                print(i,j)
            
    print("Target value greater than any pair.")


findPair([0,3,5,2,7,1,6,6,7,9],20)