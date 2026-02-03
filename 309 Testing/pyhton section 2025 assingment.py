counter = 0 
decision = "Y"
import random
mysteryFruits = ["blueberry", "apple", "bannana", "mango", "strawberry", "kiwi", "orange", "peach", "pineapple"]

while decision == "Y" and counter < 6: 
    fruits = str(input("please enter your choices of fruits"))
    while len(fruits) <4:
        print("invalid amount of charactrrs please enter a fruit with more than 4 characters") 
fruits = str(input("please enter" "Y"or "N"))

numbers = random.randint(0,9)
print("the number of fruits you entered was")
print(fruits)
print("the myster fruit was")
print(mysteryFruits)

counter = counter+1 

if counter > 3:
    print("milkshake")
elif counter ==3 or counter == 4:
    print("smoothie")
else:
    print("fruit juice")







