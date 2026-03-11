if __name__ == '__main__':
    s = input()
    print(any(item.isalnum() for item in s))
    print(any(item.isalpha() for item in s))
    print(any(item.isdigit() for item in s))
    print(any(item.islower() for item in s))
    print(any(item.isupper() for item in s))

# ------------- Other
    s = input()
    actions = ['isalnum','isalpha','isdigit','islower','isupper']
    for action in actions:
        print(any([getattr(string,action)() for string in s]))

# ------------- Other
    s = input()
    mylist = [False] * 5
    for i in s:
        if i.isalnum():
            mylist[0] = True
        if i.isalpha():
            mylist[1] = True
        if i.isdigit():
            mylist[2] = True
        if i.islower():
            mylist[3] = True
        if i.isupper():
            mylist[4] = True
            
    for j in mylist:
        print(j)