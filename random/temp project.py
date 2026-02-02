averagetemprature = []
temprature = []
for index in range (5):
    while temprature < -20 or temprature >50 :
        print ("this was not a va;lid temprature")
        temp = int (input("enter the temprature"))
    temprature.append(temp)