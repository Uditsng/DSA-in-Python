# printing average of user input values
total = 0
count = 0
while True:
    num = input("Enter number : ")
    if num == 'done':
        break
    value = float(num)
    total = total + value
    count = count + 1
    average = total / count

print("Average : ",average)

#print average of list
mylist1 = [1,2,3,4,5,6,7,8,9]
print(sum(mylist1))
print(len(mylist1))
print("Avg : ",sum(mylist1) / len(mylist1))

#taking input and print average of a list
mylist2 = []
while True:
    num = input("Enter the Num : ")
    if num == 'done': break
    num = float(num)
    mylist2.append(num)

print("Avg :", sum(mylist2) / len(mylist2))