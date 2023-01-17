# Exercise 2
stringOneInput = input("Enter a string: ")
stringTwoInput = input("Enter a second string: ")
if stringOneInput.endswith(stringTwoInput) or stringTwoInput.endswith(stringOneInput):
    print("True")
else:
    print ("False")
