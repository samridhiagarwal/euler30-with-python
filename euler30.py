TotalSum = 0    
Value = []                             #values to be added

#Range we got and then comparing the values according to criteria
for i in range(10, 354294): 
    Sum = 0                       #This sum is for getting one single value 
    for x in Str(i):
        Sum += int(x) ** 5        #checking for main condition with power 5 
    if Sum == i:                  #If the sum matches with the value 
        Value.append(i)           #The value we are in search for 

# We add those values stored in the list to get totalsum
for i in Value:
    TotalSum += i

print ("Values :" , Value)
print ("TotalSum :" , TotalSum)
