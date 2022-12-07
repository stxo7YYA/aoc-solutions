f = open('input', 'r').read().split('$')[1:]

def recurse(n):
    for i in range(len(path)):
        key = str(path[:len(path) - i])
        if key in cache:
            cache[key] += n
        else:
            cache[key] = n

path = []
cache = dict()
for seg in f:
    lns = seg.split('\n')
    cmd = lns[0].split()
    if cmd[0] == 'cd':
        if cmd[1] == '..':
            path.pop()
        else:
            path.append(cmd[1])
    if cmd[0] == 'ls':
        n = 0
        for i in range(1, len(lns) - 1):
            if not lns[i]:
                break
            spl = lns[i].split()
            if spl[0] != 'dir':
                n += int(spl[0])
        recurse(n)

one = 0
for path in cache:
    size = cache[path]
    if size <= 100000:
        one += size
print('Part One', one)

required = 30000000
delete = required - (70000000 - cache["['/']"])
two = required
for path in cache:
    size = cache[path]
    if size >= delete:
        two = min(two, size)
print('Part Two', two)
