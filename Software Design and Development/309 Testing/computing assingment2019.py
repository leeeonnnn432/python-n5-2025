import random

endings = ["ing","end","axe","gex","goh"]
studentsNo = int(input("enter the number of students that need passwords"))
for i in range(studentsNo):
    name = input("enter first three letters of the name ")
    while len(name) != 3 :
        print("invalid name")
        name = input("enter first three letters of the name ")
    number=random.randint(0,4)
    username = (name+endings[number])
    print("your username is,",username) 

   