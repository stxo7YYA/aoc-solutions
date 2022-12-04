f = open('input', 'r')
l = [x.strip() for x in f][:-1]
f = lambda c: ord(c) - 96 if c.islower() else ord(c) - 38
one = 0
two = 0
for s in l:
    one += f((set([*s[:len(s)//2]]) & set([*s[len(s)//2:]])).pop())
for i in range(2, len(l), 3):
    two += f((set([*l[i - 2]]) & set([*l[i - 1]]) & set([*l[i]])).pop())
print('Part One', one)
print('Part Two', two)
