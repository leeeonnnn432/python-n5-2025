password = input("Please enter your password: ")
while len(password) < 8:
    print("your not good enough try a password with over 8 characters")
    password = input("Please enter your password: ")
print("Password accepted.")
