def print_formatted(number):
    for num in range(1,number+1):
        decimal = num # decimal
        octal = f"{num:o}" # Octal
        hexadecimal = f"{num:x}".upper() # hexadecimal
        binary = f"{num:b}" # binary
        print(f"{decimal} {octal} {hexadecimal} {binary}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)