# python3
import queue

class tree:
    def __init__(self, parent, child, height, visited):
        self.parent = None
        self.child = None
        self.height = None
        self.visited = None

def compute_height(n, parents):
    l = [tree(None, None, None, 0) for i in range(n)]
    root = 0
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            a = parents[i]
            l[i].parent = a
            if l[a].child is None:
                l[a].child = [i]
            else:
                l[a].child.append(i)

    que = queue.Queue(maxsize = n)
    height_tree = 0
    l[root].height = 1
    l[root].visited = 1
    que.put(root)
    while que.empty() == False:
        a = que.get()
        if l[a].child:
            for i in l[a].child:
                if l[i].visited is None:
                    que.put(i)
                    l[i].height = l[l[i].parent].height + 1
                    l[i].visited = 1
                    height_tree = max(height_tree, l[i].height)

    return height_tree

def main():
    n = int(input())
    parents = input()
    parents = list(map(int, parents.split()))
    print(compute_height(n, parents))

if __name__ == "__main__":
    main()
