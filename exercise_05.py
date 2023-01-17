# Exercise 5
j = int(0)
k = int(0)
numInput = int
List2 = []
List3 = []
List4 = []
while (5>j):
    numInput = int(input("Enter a number for the first list: "))
    List2.append(numInput)
    j = j + 1
while (5>k):
    numInput = int(input("Enter a number for the second list: "))
    List3.append(numInput)
    k = k + 1
List4 = set(List2).intersection(List3)
#Turn the set back into list for what you want
List4 = list(List4)
print(List4)
