#A
n = int(input())
i = 1

while i * i <= n:
    print(i * i)
    i += 1
    
#B
n = int(input())

for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        break
    
#C
n = int(input())
power = 1

while power <= n:
    print(power, end=' ')
    power = power * 2
    
#D
n = int(input())

while n > 0 and n % 2 == 0:
    n = n // 2

if n == 1:
    print("YES")
else:
    print("NO")
    
#E
n = int(input())
power = 1
k = 0

while power < n:
    power = power * 2
    k += 1

print(k)