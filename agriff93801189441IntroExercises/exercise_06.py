# Exercise 6
ZeroList1 = [0,0,0,0,0]
ZeroList2 = [0,0,0,0,0]
ZeroList3 = [0,0,0,0,0]
ZeroList4 = [0,0,0,0,0]
ZeroList5 = [0,0,0,0,0]
zeroListRowInput = int(input("Enter a row num from 1 to 5: "))
zeroListColInput = int(input("Enter a col num from 1 to 5: ")) 
zeroListColInput = zeroListColInput-1

if zeroListRowInput == 1:
    ZeroList1[zeroListColInput] = 1
if zeroListRowInput == 2:
    ZeroList2[zeroListColInput] = 1
if zeroListRowInput == 3:
    ZeroList3[zeroListColInput] = 1
if zeroListRowInput == 4:
    ZeroList4[zeroListColInput] = 1
if zeroListRowInput == 5:
    ZeroList5[zeroListColInput] = 1
print(str(ZeroList1)[1:-1])
print(str(ZeroList2)[1:-1])
print(str(ZeroList3)[1:-1])
print(str(ZeroList4)[1:-1])
print(str(ZeroList5)[1:-1])
