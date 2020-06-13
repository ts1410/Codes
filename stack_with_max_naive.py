#python3
import sys

if __name__ == '__main__':
    num_queries = int(sys.stdin.readline())
    stack = []
    max_stack = []
    query = []
    for _ in range(num_queries):
        query.append(sys.stdin.readline().split())
    for i in query:
        if i[0] == 'max':
            print(max_stack[len(stack) - 1])
        elif i[0] == 'pop':
            stack.pop()
        else:
            stack.append(i[1])
            if len(max_stack) == 0:
                max_stack.append(i[1])
            elif (max_stack[len(max_stack) - 1] > i[1]):
                max_stack.append(max_stack[len(max_stack) - 1])
            else:
                max_stack.append(i[1])
