f = open('input', 'r')
f = [x for x in f]
n = (len(f[0]) + 1) // 4
s = [[] for _ in range(n)]
t = [[] for _ in range(n)]
tmp = []
for i in range(len(f)):
    ln = f[i]
    if ln == '\n':
        sep = i + 1
        break
    tmp.append([ln[j] for j in range(1, len(ln), 4)])
for i in range(len(tmp) - 2, -1, -1):
    for j in range(n):
        if tmp[i][j] != ' ':
            s[j].append(tmp[i][j])
            t[j].append(tmp[i][j])
for i in range(sep, len(f) - 1):
    ln = f[i].split()
    n, src, dst = [int(x) for x in [ln[1], ln[3], ln[5]]]
    src -= 1
    dst -= 1
    for j in range(n):
        s[dst].append(s[src][-1])
        s[src].pop()
    for j in range(n, 0, -1):
        t[dst].append(t[src][-j])
    for j in range(n):
        t[src].pop()
print('Part One', ''.join([x[-1] if len(x) else '-' for x in s]))
print('Part Two', ''.join([x[-1] if len(x) else '-' for x in t]))
