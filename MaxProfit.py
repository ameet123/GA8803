def max_profit(a, p, k):
    print "# of locations:{} # of p:{}".format(len(a), len(p))
    P = [p[0]]
    seq = [[a[0]]]
    for i in range(1, len(a)):
        max_profit = p[i]
        max_j = -1
        for j in range(0, i):
            dist = a[i] - a[j]
            if dist >= k:
                candidate_profit = P[j] + p[i]
            else:
                candidate_profit = P[j]
            print "j={} i:{} p[i]:{} max_profit:{} cand_profit:{}".format(j, i, p[i], max_profit, candidate_profit)
            if candidate_profit > max_profit:
                max_profit = candidate_profit
                max_j = j
        if max_j < 0:
            b = list([a[i]])
        else:
            b = list(seq[max_j])
            b.append(a[i])
        print "a[i]:{} at {}-> max_j={}".format(a[i], i, max_j)
        P.insert(i, max_profit)
        seq.insert(i, b)

    print "***** {}".format(seq[len(a) - 1])
    for l in seq:
        print ">> {}".format(l)


if __name__ == '__main__':
    a = [10, 21, 32, 40, 53, 60, 71, 83, 90, 104, 118, 120, 132]
    p = [100, 110, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    # p = [90, 82, 102, 99, 120, 77, 82, 88, 100, 94, 109, 111, 66]
    k = 12
    max_profit(a, p, k)
