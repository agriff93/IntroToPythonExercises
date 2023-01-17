# Exercise 4
averageInput = int(input("Enter a number: "))
k = int(1)
List = []
while (averageInput>=k):
    numInput = float(input("Enter number " + str(k) + ": "))
    List.append(numInput)
    k = k + 1
print(List)
print(sum(List)/len(List))

