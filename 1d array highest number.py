scores = [75, 82, 93, 65, 78]
highestscore = scores[0]
for index in range (1,len(scores)):
    if scores[index] > highestscore:
        highestscore = scores[index]
print ("the highest score is",highestscore)
