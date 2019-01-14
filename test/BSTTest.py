from copy import deepcopy

from BST import Graph

# all words frequencies
f = [.05, .4, .08, .04, .1, .1, .23]


def testGraph():
    g0 = Graph(f, 0)
    g0.BFS()


def testInject():
    g0 = Graph(f, 0)
    g0_cp = deepcopy(g0)
    g0_cp.injectNodeAt(1, 0)
    g0_cp.BFS()


def testInjectAtNegative():
    g0_cp = Graph(f, 0)
    g0_cp.injectNodeAt(1, -1)
    g0_cp.printNodes()
    g0_cp.BFS()

    # add else
    g0_cp.injectNodeAt(2, 0)
    g0_cp.printNodes()
    g0_cp.BFS()
    # # at i=1
    g0_cp.injectNodeAt(2, 1)
    g0_cp.printNodes()
    g0_cp.BFS()
    # # add end
    g0_cp2 = deepcopy(g0_cp)
    g0_cp2.injectNodeAt(3, -1)
    g0_cp2.printNodes()
    g0_cp2.BFS()
    # # at 2
    g0_cp2 = deepcopy(g0_cp)
    g0_cp2.injectNodeAt(3, 2)
    g0_cp2.printNodes()
    cost=g0_cp2.BFS()
    assert cost==.78
