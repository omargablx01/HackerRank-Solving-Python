def swap_case(s):
    new_swap = []
    for i in s :
        if i == i.upper():
            i = i.lower()
            new_swap.append(i)
        else:
            i = i.upper()
            new_swap.append(i)
            
    return "".join(new_swap)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)