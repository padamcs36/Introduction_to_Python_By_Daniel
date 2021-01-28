marks = [50, 80, 90, 78, 34, 30]
std_name = []
std_mark = []
# with open("Ex_10_Textfile", mode="r") as f:
#     for i in f:
#         marks.append(i)
# print(marks)

for i in range(5):
    std_name.append(input("Student Name: "))
    std_mark = marks[i]
for i in range(5):
    if std_mark[i] > std_mark [i+1]:
        std_mark [i+1] = std_mark[i]
    print(std_mark[i])