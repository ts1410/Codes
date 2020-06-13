# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    l = []
    for i in range(len(weights)):
        l.append([weights[i], values[i]])
    l.sort(key = lambda x:x[1]/x[0], reverse = True)
    i = 0
    while capacity and i<len(l):
        a = min(l[i][0], capacity)
        value += a*(l[i][1]/l[i][0])
        capacity -= a
        i += 1

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
