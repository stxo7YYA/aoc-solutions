f = open('input', 'r').readlines()[0][:-1]
for i in range(len(f)):
    if i + 3 < len(f):
        s = set()
        for j in range(0, 4):
            s.add(f[i + j])
        if len(s) == 4:
            print('Part One', i + 4)
            break
for i in range(len(f)):
    if i + 13 < len(f):
        s = set()
        for j in range(0, 14):
            s.add(f[i + j])
        if len(s) == 14:
            print('Part Two', i + 14)
            break
