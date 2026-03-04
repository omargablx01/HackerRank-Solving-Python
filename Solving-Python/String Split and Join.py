def split_and_join(line):
    my_split = line.split()
    my_join = "-".join(my_split)
    return my_join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)