from __future__ import print_function

import sys
from copy import deepcopy


class Graph:
    def __init__(self, frequencies, root):
        self.frequencies = frequencies
        self.rootNode = self.Node(root)
        self.nodes = {root: self.rootNode}

    def toStr(self):
        graphString = "{ "
        for n in self.nodes:
            graphString = graphString + str(n) + "-> "
        graphString = graphString + " }"
        return graphString

    def printNodes(self):
        print(self.toStr())

    def getNode(self, x):
        n = self.nodes.get(x)
        if n is None:
            n = self.Node(x)
            self.nodes[x] = n
        return n

    def addEdge(self, u, v):
        uN = self.getNode(u)
        vN = self.getNode(v)
        if u > v:
            uN.left = vN
        else:
            uN.right = vN
        print("Adding source node:{}".format(uN.toStr()))
        if v == self.rootNode.id:
            print("\t>> Changing root {}->{}".format(self.rootNode.id, u))
            self.rootNode = uN

    def injectNodeAt(self, x, i):
        print("{}\n>>Injecting node:{} at:{}".format('-' * 50, x, i))
        if i < 0:
            self.addEdge(x, self.rootNode.id)
            return True
        queue = [self.rootNode]
        print(">>Root node:{}".format(self.rootNode.id))
        isReplaced = False
        while queue:
            s = queue.pop(0)
            print("\t\t\toperating on node:{}".format(s.toStr()))
            if s.id == i:
                if x > s.id:
                    replace = s.right
                    dir = "R"
                else:
                    replace = s.left
                    dir = "L"
                print("\t\t\t>> Found my place:{} replacing {}".format(i, dir))
                if replace is not None:
                    self.addEdge(x, replace.id)
                self.addEdge(s.id, x)
                isReplaced = True
            else:
                if s.left is not None and x < s.id:
                    queue.append(s.left)
                if s.right is not None and x > s.id:
                    queue.append(s.right)
        if not isReplaced:
            print("** at:{} node:{} not found".format(i, x))
        return isReplaced

    def BFS(self):
        queue = [self.rootNode, None]
        level = 1
        cost = 0
        while queue:
            s = queue.pop(0)
            # print(">> Got node from q:{}".format(s.id))
            if s is None:
                level = level + 1
                queue.append(None)
                if queue[0] is None:
                    break
                else:
                    continue

            cost = cost + level * self.frequencies[s.id]
            print("\t\t\tlevel={} cost={}".format(level, cost))
            # get adjacent vertices
            if s.left is not None:
                queue.append(s.left)
            if s.right is not None:
                queue.append(s.right)
        print(">> Total cost:{}".format(cost))
        return cost

    class Node:
        def __init__(self, v):
            self.id = v
            self.left = None
            self.right = None

        def toStr(self):
            return "[{}]-> L:{} R:{}".format(self.id, "None" if self.left is None else self.left.id,
                                             "None" if self.right is None else self.right.id)


if __name__ == '__main__':
    # all
    f = [.05, .4, .08, .04, .1, .1, .23]
    g0 = Graph(f, 0)
    T = [g0]

    for i in range(1, len(f)):
        g_prev = T[i - 1]
        print("i={} nodes:{}\n{}".format(i, g_prev.toStr(), '-' * 15))
        cost = sys.maxint
        cur_tree = g_prev
        for j in range(-1, i):
            g_prev_cp = deepcopy(g_prev)
            print("\tj={}".format(j))
            isFound = g_prev_cp.injectNodeAt(i, j)
            print("\t\t>> j={} i={} isFound:{}".format(j, i, isFound))
            if not isFound:
                continue
            cur_cost = g_prev_cp.BFS()
            if cur_cost < cost:
                cost = cur_cost
                cur_tree = g_prev_cp
        print(">>at index:{} => min cost={}".format(i, cost))
        T.insert(i, cur_tree)
