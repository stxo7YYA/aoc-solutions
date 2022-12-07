f = open('input', 'r').read().split('$')[1:]

path = list()
cache = dict()

for x in f:
    y = x.split('\n')
    cmd = y.pop(0).split()

    ''' Update path '''
    if cmd[0] == 'cd':
        path.pop() if cmd[1] == '..' else path.append(cmd[1])

    ''' Process file sizes '''
    if cmd[0] == 'ls':

        ''' Determine the total size of visible files '''
        size = 0
        for z in y:
            if not z:
                break
            data = z.split()
            if data[0] != 'dir':
                size += int(data[0])

        ''' Propagate the total size through the path '''
        for i in range(len(path)):
            key = str(path[:len(path) - i]) # Key must be hashable
            cache.setdefault(key, 0)
            cache[key] += size

print('Part One', sum(filter(lambda n: n <= 100000,
                             [cache[path] for path in cache])))
print('Part Two', min(filter(
    lambda n: n >= 30000000 - (70000000 - cache["['/']"]),
    [cache[path] for path in cache])))
