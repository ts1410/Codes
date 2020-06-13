# Uses python3
import sys

# def get_majority_element(a, left, right):
#     a.sort()
#     if len(a) % 2 == 0:
#         m = len(a)//2
#     else:
#         m = len(a)//2
#         m += 1
#     for i in range(m):
#         if a[i + len(a)//2] == a[i]:
#             return 1
#     return -1

def get_majority_element(a, left, right):
    if right - left == 3:
        if (a[left:right].count(a[left]) >= 2):
            return a[left]
        elif (a[left:right].count(a[left + 1]) >= 2):
            return a[left + 1]
        elif (a[left:right].count(a[right - 1]) >= 2):
            return a[right - 1]
        else:
            return -1
    elif right - left == 2:
        if (a[left:right].count(a[left]) == 2):
            return a[left]
        else:
            return -1
    else:
        mid = left + (right - left)//2
        left_maj = get_majority_element(a, left, mid)
        right_maj = get_majority_element(a, mid, right)
        if(left_maj == right_maj):
            return left_maj
        else:
            l = a[left:right].count(left_maj)
            r = a[left:right].count(right_maj)
            if l == r:
                return -1
            else:
                if(l>(right - left)//2):
                    return left_maj
                elif(r>(right - left)//2):
                    return right_maj
                return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
