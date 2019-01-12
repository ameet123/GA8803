def makeValue(B, W):
    C = [0 for _ in range(0, W + 1)]
    I = [0 for _ in range(0, W + 1)]
    for b in range(1, W + 1):
        print "Capacity:{}".format(b)
        for i in range(len(B)):
            xi = B[i]
            print "\t\t>>count={} | b = {} xi = {} (b-xi) = {}  C(b)={} possible_C= {}". \
                format((b - xi), b, xi, (b - xi), C[b], xi + C[b - xi])
            if xi <= b and C[b] <= xi + C[b - xi]:
                C[b] = xi + C[b - xi]
                if (I[b]> (1+I[b-xi]) or I[b]==0) and b==C[b]:
                    I[b] = 1 + I[b - xi]
    print C
    print I


if __name__ == '__main__':
    B = [5, 10]
    W = 55  # value to make
    makeValue(B, W)
