f = list(open('input', 'r'))[0][:-1]

def solution(n: int) -> int:
    for i in range(len(f)):
        if i + n <= len(f) and len({*f[i:i + n]}) == n:
            return i + n

print('Part One', solution(4))
print('Part Two', solution(14))
