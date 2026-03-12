n, m= map(int, input().split())

w = "WELCOME"

pattern = ".|."

for i in range(n//2):
    print((pattern*(2*i+1)).center(m,"-"))

print(w.center(m, '-'))

for i in range(n//2-1, -1, -1):
    print((pattern*(2*i+1)).center(m, '-'))
    
# ---------------- Other

n, m = map(int, input().split())

w = "WELCOME"

pattern = ".|."

for i in range(1, n, 2):
    print((pattern * i).center(m, "-"))

print(w.center(m, "-"))

for i in range(n-2, -1, -2):
    print((pattern * i).center(m, "-"))