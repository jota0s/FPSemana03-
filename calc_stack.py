from collections import deque

numInput = input()

num = list(map(int,numInput.split()))

stack = deque(num)

print(f"deque({list(stack)})")

while stack:
    print(stack.pop() ** 2)