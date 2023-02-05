questions = 8
student1 = [2, 3, 6, 7]
student2 = [1, 6, 7, 8]
stud1 = set(student1)
answer = stud1.union(student2)
new_list = []
for i in range(1, questions + 1):
    if i not in answer:
        new_list.append(i)
print(list(new_list))