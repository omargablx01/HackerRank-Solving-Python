def print_formatted(number):
    my_len = len(f"{number:b}")
    
    for each in range(1,number+1) :
        decimal = f"{each:d}".rjust(my_len) # Decimal
        
        octal = f"{each:o}".rjust(my_len) # Octal
        
        hexadecimal  = f"{each:x}".upper().rjust(my_len) # Hexadecimal 
        
        binary  = f"{each:b}".rjust(my_len) # Binary 
        
        print(decimal,octal,hexadecimal,binary)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
# ! ----------- Other 

def print_formatted(number):
  
  w = len(f"{number:b}")

  for each in range(1, number+1):

    print(f"{each:d}".rjust(w),f"{each:o}".rjust(w),f"{each:x}".upper().rjust(w),f"{each:b}".rjust(w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)