cost = float(input("Enter cost of the item in £ and p: "))
noPounds = int(cost)+1
print("You will need £"+str(noPounds))
print("And you will get "+(round(noPounds-cost,2))+"p change")
