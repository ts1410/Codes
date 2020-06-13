# Uses python3
import sys

def min_op(n):
    a = [[0 for i in range(2)] for x in range(n*3 + 2)]
    a[1] = [0, 'a']
    for i in range(1, n + 1):
        if a[i + 1][0] == 0:
            a[i + 1] = [a[i][0] + 1, 'a']
        elif a[i][0] + 1 < a[i + 1][0]:
            a[i + 1] = [a[i][0] + 1, 'a']
        if a[2*i][0] == 0:
            a[2*i] = [a[i][0] + 1, 'b']
        elif a[i][0] + 1 < a[2*i][0]:
            a[2*i] = [a[i][0] + 1, 'b']
        if a[3*i][0] == 0:
            a[3*i] = [a[i][0] + 1, 'c']
        elif a[i][0] + 1 < a[3*i][0]:
            a[3*i] = [a[i][0] + 1, 'c']

    l = [n]
    i = n
    while i != 1:
        if a[i][1] == 'c':
            i = i//3
            l.append(i)
        elif a[i][1] == 'b':
            i = i//2
            l.append(i)
        else:
            i = i - 1
            l.append(i)

    return l[::-1]

def optimal_sequence(n):
    sequence = []
    if n == 1:
        return [1]
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(min_op(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
