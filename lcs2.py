#Uses python3

import sys

def lcs2(s, t):
    #write your code here
    if s == t:
        return 0
    rows = len(t)
    cols = len(s)
    d = [[0 for i in range(cols + 1)] for x in range(rows + 1)]
    for i in range(1, rows + 1):
        d[i][0] = i
    for i in range(1, cols + 1):
        d[0][i] = i
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if s[j - 1] == t[i - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                mini = min(d[i - 1][j], d[i][j - 1])
                d[i][j] = 1 + min(mini, d[i - 1][j - 1])

    seqrows = ""
    print(end = "     ")
    for i in s:
        print(i, end = "    ")
    print()

    for i in d:
        for j in i:
            print(j, end = "    ")
        print()
    i = rows
    j = cols
    seqcols = ""
    while i > 0 or j > 0:
        if d[i][j] == d[i - 1][j - 1]:
            seqrows += str(t[i - 1])
            seqcols += str(s[j - 1])
            i -= 1
            j -= 1
        elif d[i][j] == d[i][j - 1] + 1:
            seqcols += str(s[j - 1])
            j -= 1
        elif d[i][j] == d[i - 1][j] + 1:
            seqrows += str(t[i - 1])
            i -= 1
        else:
            i -= 1
            j -= 1

    ans = ""
    seqrows = seqrows[::-1]
    i = 0
    j = 0
    print(seqrows, s)
    while s:
        print(i, j, seqrows[i], s[j], ans)
        if seqrows[i] == s[j]:
            ans += s[j]
            s = s[j+1:]
            seqrows = seqrows[i+1:]
            i = 0
            j = 0
            print('equal')
            continue
        else:
            print('unequal')
            j += 1
        if j == len(s) and i != len(seqrows) - 1:
            i += 1
            j = 0
            print('both')
        elif i == len(seqrows) - 1 and j != len(s):
            print('i')
            j = 0
        elif i == len(seqrows) - 1 and j == len(s):
            break

    print('ans', ans)
    return ans

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(str, input.split()))

    n = int(data[0])
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = int(data[0])
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
