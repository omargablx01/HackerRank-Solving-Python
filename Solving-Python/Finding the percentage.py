if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.keys() :
        if query_name == i:
            my_sym = sum(student_marks[query_name])/3
            print(f"{my_sym:.2f}")