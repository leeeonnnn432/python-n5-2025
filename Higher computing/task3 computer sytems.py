character = input("Enter an ASCII character")

while len(character) != 1:
    print("Please enter only one character.")
    character = input("Enter character")

ordinal = ord(character)

print("The ordinal value is:", ordinal)