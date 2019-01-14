from __future__ import print_function

from copy import deepcopy


class Graph:
    def __init__(self, frequencies, root):
        self.frequencies = frequencies
        self.rootNode = self.Node(root)
        self.nodes = {root: self.rootNode}

    def print(self):
        for n in self.nodes:
            print(n, end=" ")
        print()

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

    def newRootCost(self, n):
        g_prev_cp = deepcopy(self)
        g_prev_cp.addEdge(n, g_prev_cp.rootNode.id)
        return g_prev_cp.BFS()

    def injectNodeAt(self, x, i):
        print("{}\n>>Injecting node:{} at:{}".format('-' * 50, x, i))
        if i < 0:
            self.addEdge(x, self.rootNode.id)
            return
        queue = [self.rootNode]
        print(">>Root node:{}".format(self.rootNode.id))
        while queue:
            s = queue.pop(0)
            print("\t\t\toperating on node:{}".format(s.toStr()))
            if s.id == i:
                if x > s:
                    replace = s.right
                    dir = "R"
                else:
                    replace = s.left
                    dir = "L"
                print("\t\t\t>> Found my place:{} replacing {}".format(i, dir))
                if replace is not None:
                    self.addEdge(x, replace.id)
                self.addEdge(s.id, x)
            else:
                if s.left is not None and x < s.id:
                    queue.append(s.left)
                if s.right is not None and x > s.id:
                    queue.append(s.right)

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
    #   begin, do , else, end
    f = [.05, .4, .08, .04]
    # list to store graphs
    # g0 = Graph(f, 1)
    # g0.addEdge(1, 0)
    # g0.addEdge(1, 2)
    # g0.BFS()
    # g_copy = deepcopy(g0)
    # g_copy.print()
    # g_copy.BFS()

    g0 = Graph(f, 0)
    g0.BFS()
    g0_cp = deepcopy(g0)
    g0_cp.injectNodeAt(1, 0)
    g0_cp.BFS()
    #
    g0_cp = deepcopy(g0)
    g0_cp.injectNodeAt(1, -1)
    g0_cp.print()
    g0_cp.BFS()
    # add else
    g0_cp.injectNodeAt(2, 0)
    g0_cp.print()
    g0_cp.BFS()

    # T = [g0]
    # for i in range(1, len(f)):
    #     if i == 2:
    #         break
    #     print("i={}\n{}".format(i, '-' * 5))
    #     g_prev = T[i - 1]
    #
    #     init_cost = g_prev.newRootCost(i)
    #     print(">> New root init cost={}".format(init_cost))
    #
    #     for j in range(0, i):
    #         # Make a copy
    #         g_prev_cp = deepcopy(g_prev)
    #         print("\tj={}".format(j))
    #         g_prev_cp.addEdge(j, i)
    #         g_prev_cp.BFS()
