# Your code here

with open("robin.txt") as f:
    words1 = f.read()
    words = words1.split()

cache = {}

for word in words:
    if word not in cache:
        cache[word] = '#'
    else:
        cache[word] += '#'

items = list(cache.items())

items.sort(key=lambda x: x[1], reverse=True)

for key, value in items:
    print(f'{key:<18} {value}')
