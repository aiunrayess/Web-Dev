N = int(input())
arr = []
for _ in range(N):
    command = input().split()
    action = command[0]
    if action == "insert":
        i = int(command[1])
        e = int(command[2])
        arr.insert(i, e)
    elif action == "print":
        print(arr)
    elif action == "remove":
        e = int(command[1])
        arr.remove(e)
    elif action == "append":
        e = int(command[1])
        arr.append(e)
    elif action == "sort":
        arr.sort()
    elif action == "pop":
        arr.pop()
    elif action == "reverse":
        arr.reverse()
