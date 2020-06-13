# Uses python3
def edit_distance(s, t):
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
    return d[rows][cols]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
