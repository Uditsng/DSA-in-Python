'''Calculate average temperature'''

numDays =int(input("Enter number of days : "))
total = 0
for i in range(1,numDays+1):
    nextDay = int(input("Days"+ str(i)+"'s high temp : "))
    total = total + nextDay
avg = total / numDays

print("\n Average: "+str(avg))