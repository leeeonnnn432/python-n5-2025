binary = ""
twos = ""

denary = int(input("What is the denary number between -128 and -1 you want to convert to binary "))

while denary > -1 or denary < -128:
    print("Please re-enter your denary number")
    denary = int(input("What is the denary number between -128 and -1 you want to convert to binary "))

denary = abs(denary)

if denary >= 128:
    binary = binary + "1"
    denary = denary - 128
else:
    binary = binary + "0"

if denary >= 64:
    binary = binary + "1"
    denary = denary - 64
else:
    binary = binary + "0"

if denary >= 32:
    binary = binary + "1"
    denary = denary - 32
else:
    binary = binary + "0"

if denary >= 16:
    binary = binary + "1"
    denary = denary - 16
else:
    binary = binary + "0"

if denary >= 8:
    binary = binary + "1"
    denary = denary - 8
else:
    binary = binary + "0"

if denary >= 4:
    binary = binary + "1"
    denary = denary - 4
else:
    binary = binary + "0"

if denary >= 2:
    binary = binary + "1"
    denary = denary - 2
else:
    binary = binary + "0"

if denary >= 1:
    binary = binary + "1"
else:
    binary = binary + "0"

for bit in binary:
    if bit == "1":
        twos = twos + "0"
    else:
        twos = twos + "1"

number = int(twos, 2)
number = number + 1

binary = bin(number)

print("Two's complement =", binary)