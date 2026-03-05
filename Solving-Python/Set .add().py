# Enter your code here. Read input from STDIN. Print output to STDOUT
my_range = int(input())
my_count = set()
for _ in range(my_range):
    my_char = input()
    my_count.add(my_char)
print(len(my_count))