two = False
f = open('inp', 'r')
data = {}


def solve(s):
    x = data[s]
    if type(x) == int:
        return x
    a = solve(x[0])
    b = solve(x[2])
    return a <= b if s == 'root' and two else {'+':a + b,
                                               '-':a - b,
                                               '*':a * b,
                                               '/':a // b}[x[1]]


for ln in f:
    if ln == '\n':
        break
    s = ln.split()
    data[s[0][:-1]] = int(s[1]) if len(s) == 2 else tuple(s[1:])
print('Part One', solve('root'))
two = True
l = 0
r = 10000000000000
while l <= r:
    m = (l + r) // 2
    data['humn'] = m
    if solve('root'):
        r = m - 1
    else:
        l = m + 1
print('Part Two', l)
