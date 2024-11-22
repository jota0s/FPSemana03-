from collections import deque

wordsInput = input()

words = wordsInput.split()

queue = deque(words)

print(f"deque({list(queue)[::-1]})")

for word in queue:
    if 'o'in word:
        print(word) 