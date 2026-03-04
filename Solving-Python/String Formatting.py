def print_formatted(number):
<<<<<<< HEAD
    for num in range(1,number+1):
        decimal = num # decimal
        octal = f"{num:o}" # Octal
        hexadecimal = f"{num:x}".upper() # hexadecimal
        binary = f"{num:b}" # binary
        print(f"{decimal} {octal} {hexadecimal} {binary}")
=======
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
>>>>>>> 527e329f40b33153be4384a8e5e6f20188adb94b

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)