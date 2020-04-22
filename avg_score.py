if __name__ == '__main__':
    total=0
    lines=[]
    student_marks = {}
    while True:
        line=input()
        if line.'isalnum':
            lines.append(line.split(' ',1))
        else:
            break

    lines.pop(0)
    student=lines.pop()
    print(str(student[0]))
    for i in range(len(lines)):
        for j in range(1,len(lines[i])):
            student_marks[lines[i].pop(0)]=lines[i]

    print(student_marks)
    scores=student_marks[student[0]][0].split()
    # print(student_marks[student[0]][0].split())
    for i in (scores):
        total+=int(i)

    avg=total/len(scores)
    print(avg)
    # for _ in range(n):
    #     name, *line = input().split()
    #     scores = list(map(float, line))
    #     student_marks[name] = scores
    # query_name = input()
