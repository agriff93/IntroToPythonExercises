# Exercise 9
WordList = []
StringWordList = str()
j = int(0)
while 5>j:
    WordListAdd = input("Enter a word: ")
    WordList.append(WordListAdd)
    StringWordList = ' '.join(WordList)
    j=j+1
print(StringWordList)