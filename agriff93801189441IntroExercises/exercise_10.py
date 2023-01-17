# Exercise 10
List = []
SeparatedList = []
StringWords = str(input("Enter a string: "))
for k in StringWords:
    List.append(k)
for j in range(0, len(List), 3):
    SeparatedList.append(List[j:j+3])
print(List)
print(SeparatedList)