#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    i = 0
    n = len(a)
    check = 0
    if not a:
        return ""
    for f in a:
        # print(i, i[0])
        if f[0] == str(0):
            check += 1
            continue
        else:
            break
    # print(a[0][0], check)
    if check == len(a):
        return "0"

    while i < n:
        i += 1
        maxi = a[0]
        max_index = 0
        if len(a) == 1:
            res += a[0]
            break
        for j in range(0, len(a)):
            if len(maxi) == len(a[j]):
                if maxi < a[j]:
                    # print(maxi, a[j], 'length')
                    maxi = a[j]
                    max_index = j
            else:
                x = 0
                y = 0
                flag = 0
                # print('maxi ', maxi)
                while x < len(maxi) and y < len(a[j]):
                    if maxi[x] < a[j][y]:
                        maxi = a[j]
                        flag = 1
                        max_index = j
                        # print('hello')
                        break
                    # elif maxi[x] > a[j][y]:
                        flag = 1
                        # print('here')
                        break
                    else:
                        # print('over here')
                        x += 1
                        y += 1
                # print('flag ', flag)
                if flag == 0:
                    # print('inside ', y, x, a[j], maxi, a[j][y - 1], maxi[len(maxi) - 1])
                    if y == len(a[j]) and a[j][y - 1] > maxi[len(maxi) - len(a[j])]:
                        # print('hi', y)
                        maxi = a[j]
                        max_index = j
                    elif x == len(maxi) and a[j][y] > maxi[len(maxi) - 1]:
                        maxi = a[j]
                        max_index = j

        res += str(maxi)
        # print(a, max_index, a[max_index], a[0])
        a[0], a[max_index] = a[max_index], a[0]
        # print(a, max_index, a[max_index], a[0])
        a = a[1:]
        # print('i is ', i)\

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))






