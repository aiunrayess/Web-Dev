#A
n = int(input())

numbers = list(map(int, input().split()))

for i in range(0, n, 2):
    print(numbers[i], end=' ')
    
#B
n = int(input())
numbers = list(map(int, input().split()))

for x in numbers:
    if x % 2 == 0:
        print(x, end=' ')
        
#C
n = int(input())
numbers = list(map(int, input().split()))

count = 0
for x in numbers:
    if x > 0:
        count += 1

print(count)

#D
n = int(input())
numbers = list(map(int, input().split()))

count = 0
for i in range(1, n):
    if numbers[i] > numbers[i-1]:
        count += 1

print(count)

#E
n = int(input())
a = list(map(int, input().split()))

found = False
for i in range(1, n):
    if (a[i] > 0 and a[i-1] > 0) or (a[i] < 0 and a[i-1] < 0):
        found = True
        break

if found:
    print("YES")
else:
    print("NO")

#F
n = int(input())
a = list(map(int, input().split()))

count = 0
for i in range(1, n - 1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        count += 1

print(count)

#G
n = int(input())
a = list(map(int, input().split()))

for i in range(n // 2):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]

for x in a:
    print(x, end=' ')