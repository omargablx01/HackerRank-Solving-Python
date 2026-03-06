# if __name__ == '__main__':
    
#     names_per_grade = {}
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         names_per_grade.setdefault(score, []).append(name)
        
#     second_lowest_grade = sorted(names_per_grade.keys())[1]
#     for name in sorted(names_per_grade[second_lowest_grade]):
#         print(name)

# -------------- Other

if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score, name])    
    records.sort()
    
    list_without_min_of_records = list(filter(lambda item: item[0] > min(records)[0], records))
    
    cleared_list = list(filter(lambda item: item[0] <= min(list_without_min_of_records)[0], list_without_min_of_records))
        
    for item in cleared_list:
        print(item[1])