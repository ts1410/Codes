# Uses python3
import sys

def optimal_weight(W, wt, val, n):
    # write your code here
    # A Dynamic Programming based Python Program for 0-1 Knapsack problem
    # Returns the maximum value that can be put in a knapsack of capacity W
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    print(K)

    return K[n][W]

        # Driver program to test above function


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, w, len(w)))
