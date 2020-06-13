# Uses python3
import sys
import random

def fast_count_segments(starts, ends, points):
    #write your code here
    l = []

    for i in range(len(starts)):
        l.append([starts[i], 'l'])
        l.append(([ends[i], 'r']))

    for i in range(len(points)):
        l.append([points[i], 'p'])

    l.sort(key = lambda x : (x[0], x[1]))

    ans = dict()
    for i in points:
        ans[i] = 0

    cnt = 0
    for i in l:
        if i[1] == 'l':
            cnt += 1
        elif i[1] == 'r':
            cnt -= 1
        else:
            ans[i[0]] = cnt

    return ans

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()

    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    a = []
    for x in points:
        a.append(cnt[x])
    for x in a:
        print(x, end=' ')
