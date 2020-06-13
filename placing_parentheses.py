# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    length = len(dataset)
    numOfnum = (length + 1)//2
    minArray = [[0 for x in range(numOfnum)] for y in range(numOfnum)]
    maxArray = [[0 for x in range(numOfnum)] for y in range(numOfnum)]
    j = 0
    for i in range(numOfnum):
        minArray[i][i] = int(dataset[j])
        maxArray[i][i] = int(dataset[j])
        j += 2
    # for i in range(numOfnum):
    #     for j in range(numOfnum):
    #         print(minArray[i][j], end = '  ')
    #     print()

    for s in range(numOfnum - 1):
        for i in range(numOfnum - s - 1):
            j = i + s + 1
            minVal = 10**4
            maxVal = -10**5
            print('here ', i, j)
            for k in range(i, j):
                print('i:', i,'k:', k,'k + 1:', k + 1,'j:', j)
                a = evalt(minArray[i][k], minArray[k + 1][j], dataset[2*k + 1])
                b = evalt(minArray[i][k], maxArray[k + 1][j], dataset[2*k + 1])
                c = evalt(maxArray[i][k], minArray[k + 1][j], dataset[2*k + 1])
                d = evalt(maxArray[i][k], maxArray[k + 1][j], dataset[2*k + 1])
                minVal = min(minVal, a, b, c, d)
                maxVal = max(maxVal, a, b, c, d)
            minArray[i][j] = minVal
            maxArray[i][j] = maxVal

    return maxArray[0][numOfnum - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
