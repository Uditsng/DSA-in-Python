''' nested loop time complexity , no matter how many nested loop are there but it is always n^2 '''

def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)

print_items(8)        

