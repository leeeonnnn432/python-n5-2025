binary=""
denary=0

denary=int(input("What is the denary number between 1-255 you want to convert to binary "))

while denary >255 or denary <0:
    print("Please re-enter your denary number")
    denary=int(input("What is the denary number between 1-255 you want to convert to binary "))

if denary >=128:
    binary += "1"
    denary -=128
else:
    binary += "0"

if denary >=64:
    binary += "1"
    denary -=64
else:
    binary += "0"

if denary >=32:
    binary += "1"
    denary -=32
else:
    binary += "0"

if denary >=16:
    binary += "1"
    denary -=16
else:
    binary += "0"

if denary >=8:
    binary += "1"
    denary -=8
else:
    binary += "0"

if denary >=4:
    binary += "1"
    denary -=4
else:
    binary += "0"

if denary >=2:
    binary += "1"
    denary -=2
else:
    binary += "0"

if denary >=1:
    binary += "1"
else:
    binary += "0"

print("Binary =", binary)