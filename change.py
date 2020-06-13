# Uses python3
import sys

def get_change(m):
    #write your code here
    n = 0
    a = [10, 5, 1]
    a = [x for x in a if x<=m]
    while m != 0:
        n += m//a[0]
        m -= a[0]*(m//a[0])
        a = a[1:]
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
