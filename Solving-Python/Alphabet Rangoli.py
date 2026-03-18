import string
def print_rangoli(size):
    alpha = [x for x in string.ascii_lowercase[:size]]
    
    beta = list(reversed(alpha))
    
    for i in range(size):
        print('-'.join(beta[:i+1] + alpha[size-i:]).center((size*2)-1+(size*2)-2, '-'))
        
    for i in range(size-2, -1, -1):
        print('-'.join(beta[:i+1] + alpha[size-i:]).center((size*2)-1+(size*2)-2, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)