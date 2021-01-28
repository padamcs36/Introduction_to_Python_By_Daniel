student = eval(input("Enter number of student: "))
scoreList = []
for i in range(student):
    score = eval(input("Enter score of student: "))
    scoreList.append(score)

# for i in range(student):
#     if scoreList[i+1] > scoreList[i]:
#         scoreList[i] = scoreList[i+1]
#     print(scoreList[i])
sorted(scoreList)
print(scoreList[0], scoreList[1])