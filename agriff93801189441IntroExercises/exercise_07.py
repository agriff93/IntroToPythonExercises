# Exercise 7
x = int(0)
QuitList = []
QuitEvenList = []
while x == 0:
    quitUserInput = input("Enter a number or QUIT to quit ")
    if quitUserInput == "QUIT":
        print(QuitList)
        x = 1
    else:
        (QuitList.append(quitUserInput))

for num in QuitList:
    if float(num) % 2 == 0:
        QuitEvenList.append(num)
print("All Nums:" + str(QuitList))
print("Even Nums:" + str(QuitEvenList))
