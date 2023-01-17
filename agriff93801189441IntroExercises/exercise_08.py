# Exercise 8
OriginalList = []
UniqueList = []
y = int(1)
z = int(0)
countedListNum = int(0)
while (10>=y):
    OriginalListAdd = input("Enter number " + str(y) + ": ")
    OriginalList.append(OriginalListAdd)
    y = y + 1
while len(OriginalList) > z:
    countedListNum = OriginalList.count(OriginalList[z])
    if countedListNum == 1:
        UniqueList.append(OriginalList[z])
    z = z + 1
print(OriginalList)
print(UniqueList)