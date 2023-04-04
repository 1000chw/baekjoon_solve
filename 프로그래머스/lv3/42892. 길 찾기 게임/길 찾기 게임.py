import sys
sys.setrecursionlimit(1000000)
class node:
    def __init__(self, n, x, depth):
        self.n = n
        self.x = x
        self.childL = []
        self.childR = []
        self.depth = depth

    def get_n(self):
        return self.n

    def get_depth(self):
        return self.depth

    def get_childL(self):
        return self.childL

    def get_childR(self):
        return self.childR

    def put_childL(self, child):
        self.childL = child

    def put_childR(self, child):
        self.childR = child

    def get_x(self):
        return self.x

def solution(nodeinfo):
    answer = []
    tmp = nodeinfo[:]
    tmp.sort(key=lambda x: x[0])
    tmp.sort(key=lambda x: x[1], reverse=True)
    order = [nodeinfo.index(i)+1 for i in tmp]
    depth = list(set([i[1] for i in nodeinfo]))
    depth.sort(reverse=True)
    for i in tmp:
        i[1] = depth.index(i[1])
    tree = node(order[0], tmp[0][0], tmp[0][1])
    for i in range(1, len(tmp)):
        xnode = tree
        cnode = node(order[i], tmp[i][0], tmp[i][1])
        while 1:
            if xnode.get_depth() + 1 == cnode.get_depth():
                if xnode.get_x() > cnode.get_x():
                    xnode.put_childL(cnode)
                else:
                    xnode.put_childR(cnode)
                break
            if xnode.get_x() > cnode.get_x():
                xnode = xnode.get_childL()
            else:
                xnode = xnode.get_childR()
    res = []
    preorder(tree, res)
    answer.append(res)
    res = []
    postorder(tree, res)
    answer.append(res)
    return answer

def preorder(tree, res):
    if not tree:
        return
    res.append(tree.get_n())
    preorder(tree.get_childL(), res)
    preorder(tree.get_childR(), res)

def postorder(tree, res):
    if not tree:
        return
    postorder(tree.get_childL(), res)
    postorder(tree.get_childR(), res)
    res.append(tree.get_n())
