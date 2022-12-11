import math

f       = open('input', 'r').read().split('\n\n')[:-1]
n       = len(f)
monkeys = []

class monkey_data:
    def __init__(self, items, operator, parameter, test, true, false):
        self.items     = items
        self.operator  = operator
        self.parameter = parameter
        self.test      = test
        self.true      = true
        self.false     = false
        self.inspected = 0

for i in range(n):
    arr       = f[i].split('\n')
    items     = [int(x) for x in arr[1][18:].split(', ')]
    operation = arr[2][23:].split()
    operator  = operation[0]
    parameter = int(operation[1]) if operation[1].isdigit() else operation[1]
    test      = int(arr[3][21:])
    true      = int(arr[4][29:])
    false     = int(arr[5][30:])
    monkeys.append(monkey_data(items, operator, parameter, test, true, false))

product = math.prod([monkey.test for monkey in monkeys])

for round in range(10000): # 20
    for i in range(n):
        monkey = monkeys[i]
        monkey.inspected += len(monkey.items)
        for item in monkey.items:
            if monkey.operator == '*':
                if monkey.parameter == 'old':
                    item *= item
                else:
                    item *= monkey.parameter
            else:
                if monkey.parameter == 'old':
                    item += item
                else:
                    item += monkey.parameter
            # item //= 3
            item %= product
            if item % monkey.test:
                monkeys[monkey.false].items.append(item)
            else:
                monkeys[monkey.true].items.append(item)
        monkey.items = []

# print('Part One', math.prod(sorted([monkey.inspected for monkey in monkeys])[-2:]))
print('Part Two', math.prod(sorted([monkey.inspected for monkey in monkeys])[-2:]))
