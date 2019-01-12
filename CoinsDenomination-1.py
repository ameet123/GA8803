def makeValue(B, W):
    C = [0 for _ in range(0, W+1)]
    for b in range(1, W+1):
        print "Capacity:{}".format(b)
        for i in range(0, len(B)):
            xi = B[i]
            print "\t\tb = {} xi = {} (b-xi) = {}  possible_C= {}".format(b, xi, (b - xi), xi + C[b - xi])
            if xi <= b and C[b] < xi + C[b - xi]:
                C[b] = xi + C[b - xi]
    print C


if __name__ == '__main__':
    B = [3]
    W = 10  # value to make
    makeValue(B, W)
