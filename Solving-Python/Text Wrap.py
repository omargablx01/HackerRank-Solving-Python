import textwrap

def wrap(string, max_width):
    
    my_result = []

    for i in range(0,len(string),max_width):
        my_result.append(string[i : i + max_width])
    
    return "\n".join(my_result)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# ---------- Other

import textwrap

def wrap(string, max_width):
    
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

