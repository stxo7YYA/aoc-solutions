f = open('input', 'r')
l = [x.strip() for x in f.readlines()][:-1]
f = lambda c: ord(c) - 96 if c.islower() else ord(c) - 38
one = 0
two = 0
for ln in l:
    s1 = set(); [s1.add(c) for c in ln[:len(ln)//2]]
    s2 = set(); [s2.add(c) for c in ln[len(ln)//2:]]
    one += f((s1 & s2).pop())
print('Part One', one)
for i in range(2, len(l), 3):
    s1 = set(); [s1.add(c) for c in l[i - 2]]
    s2 = set(); [s2.add(c) for c in l[i - 1]]
    s3 = set(); [s3.add(c) for c in l[i]]
    two += f((s1 & s2 & s3).pop())
print('Part Two', two)
