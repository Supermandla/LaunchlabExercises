theArray = [0,1,2,3,5,2]
k = 3
indexForNums = []
for i in range(0, len(theArray)):
    if theArray[i] == 2:
        indexForNums.append(i)
print(indexForNums)
if (indexForNums[0] - indexForNums[1])<=k:
    print("Contains close numbers")
else:
    print("Does Not contain close numbers")
    
    
