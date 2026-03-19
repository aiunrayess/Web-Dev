#A
def min4(a, b, c, d):
    res = a
    if b < res:
        res = b
    if c < res:
        res = c
    if d < res:
        res = d
    return res

a, b, c, d = map(int, input().split())
print(min4(a, b, c, d))

#B
def power(a, n):
    res = 1.0
    for i in range(n):
        res *= a
    return res

a, n = map(float, input().split())
print(power(a, int(n)))

#C
def xor(x, y):
    if x != y:
        return 1
    else:
        return 0

x, y = map(int, input().split())
print(xor(x, y))