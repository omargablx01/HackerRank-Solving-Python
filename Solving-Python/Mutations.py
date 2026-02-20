def mutate_string(string, position, character):
    s_list = list(string)
    s_list[position] = character
    result = "".join(s_list)
    return result
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)