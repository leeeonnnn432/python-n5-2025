thisArray=["kirtsy", "amelia", "james", "ali", "euan", "joshuaa"]
mostcharacters=len(thisArray[0])
pos = 0
for index in range(1,len(thisArray)):
    if len (thisArray[index]) > mostcharacters:
        mostcharacters = len(thisArray[index])
        pos = index 
    print("the name with the most characters:", mostcharacters)

