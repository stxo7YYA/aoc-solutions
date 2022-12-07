f = open('input', 'r').read().split('$')[1:]

path = list()
cache = dict()

for x in f:
    y = x.split('\n')
    cmd = y[0].split()

    # Update path
    if cmd[0] == 'cd':
        if cmd[1] == '..':
            path.pop()
        else:
            path.append(cmd[1])

    # Process file sizes
    if cmd[0] == 'ls':

        # Determine the total size of visible files
        size = 0
        for i in range(1, len(y) - 1):
            if not y[i]:
                break
            data = y[i].split()
            if data[0] != 'dir':
                size += int(data[0])

        # Propagate the total size through the path
        for i in range(len(path)):
            key = str(path[:len(path) - i])
            if key in cache:
                cache[key] += size
            else:
                cache[key] = size

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
