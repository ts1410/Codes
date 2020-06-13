# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops = [0] + stops + [distance]
    num = 0
    currentrefill = 0
    while currentrefill < len(stops) - 1:
        lastrefill = currentrefill
        while stops[currentrefill] < distance and stops[currentrefill+1] - stops[lastrefill] <= tank:
            currentrefill += 1
        if currentrefill == lastrefill:
            return -1
        elif stops[currentrefill] < distance:
            num += 1

    return num

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
