f = open('input', 'r').read()[:-1]
lst = [sum([int(x) for x in x.strip().split('\n')]) for x in f.split('\n\n')]
lst.sort()
print('Part One', max(lst))
print('Part Two', sum(lst[-3:]))
