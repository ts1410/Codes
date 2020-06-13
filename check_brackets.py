# python3

from collections import deque
from collections import namedtuple

brackets = namedtuple('brackets', ['char', 'pos'])

def find_mismatch(text):
    stack = deque()
    l = 0
    for next in text:
        l += 1
        if next in "([{":
            # Process opening bracket, write your code here
            ans = brackets(next, l)
            stack.append(ans)
        elif next in ")]}":
            # Process closing bracket, write your code here
            if len(stack) == 0:
                return l
            elif  next == ")" and stack.pop().char != "(" or next == "]" and stack.pop().char != "[" or next == "}" and stack.pop().char != "{":
                return l

    if len(stack) == 0:
        return 'Success'
    else:
        return stack.pop().pos

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
