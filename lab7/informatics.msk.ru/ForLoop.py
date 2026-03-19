#A
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=' ')
        
#B
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a, b + 1):
    if i % d == c:
        print(i, end=' ')
        
#C
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if int(i**0.5)**2 == i:
        print(i, end=' ')
        
#G
x = int(input())

for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break  
    
#H
x = int(input())

for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=' ')
        
#I
x = int(input())
count = 0

for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        if i * i == x:
            count += 1    
        else:
            count += 2   
            
print(count)

#J
total = 0

for i in range(100):
    num = int(input())
    total += num

print(total)

#K
n = int(input())
total = 0

for i in range(n):
    num = int(input())
    total += num

print(total)

#M
n = int(input())
zeros_count = 0

for i in range(n):
    num = int(input())
    if num == 0:
        zeros_count += 1

print(zeros_count)