def pen(x):
    return (200 - x) ** 2


def optimal_penalty(a):
    P = [pen(a[0])]
    seq = [[a[0]]]
    for i in range(1, len(a)):
        opt_i_pen = pen(a[i])
        opt_j = -1
        for j in range(0, i - 1):
            cur_prev_pen = P[j] + pen(a[i] - a[j])

            if cur_prev_pen < opt_i_pen:
                opt_i_pen = cur_prev_pen
                opt_j = j
        P.insert(i, opt_i_pen)
        b = list(seq[opt_j])
        b.append(a[i])
        seq.insert(i, b)
        print "{}->{}".format(i, opt_j)
    print "***** {}".format(seq[len(a) - 1])
    for l in seq:
        print ">> {}".format(l)


if __name__ == '__main__':
    # a = [10, 21, 40, 60, 90, 120, 250]
    a = [210, 300, 350, 500, 600, 700, 800, 1000, 1300, 1800, 2500]
    optimal_penalty(a)
