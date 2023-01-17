# Alexander Griffin, 3155 151
# Exercise 1
gradeInput = int()
gradeInput = int(input("Enter grade from 0 to 100: "))
if 100 > gradeInput and gradeInput > 89:
    print ("Your Grade is an A")
if 90 > gradeInput and gradeInput > 79:
    print ("Your Grade is a B")
if 80 > gradeInput and gradeInput > 69:
    print ("Your Grade is a C")
if 70 > gradeInput and gradeInput > 59:
    print ("Your Grade is a D")
if gradeInput < 60:
    print ("Your Grade is an F")


