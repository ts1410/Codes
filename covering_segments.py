# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    sorted_segments = sorted(segments, key=lambda x: x.end)

    points = []
    while sorted_segments:
        # Place the first point to the right endpoint of the first segment.
        # Remove the segment, since it's considered as covered one.
        segment = sorted_segments.pop(0)
        point = segment.end
        points.append(point)

        # Check whether the point hit the other segments.
        for s in sorted_segments[:]:
            if s.start <= point <= s.end:
                sorted_segments.remove(s)

    return points
    # count = len(segments)
    # segments.sort(key = lambda  x : (x.start, x.end))
    # l = []
    # while count:
    #     t = segments[0].end
    #     n = sum(map(lambda x : x.start <= t, segments))
    #     l.append(min(segments[:n], key = lambda x : x.end)[1])
    #     count -= n
    #     for j in range(n):
    #         del segments[0]
    #
    # return l

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
