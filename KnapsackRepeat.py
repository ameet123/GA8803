# for a given iteration, i.e. a given capacity b,
# we don't check a specific weight wi multiple times.
# although it may seem that we should be doing that, that's not the algorithm.
# instead we rely on previously constructed values in table.
# now , previously we may have used that same weight and in this fashion,
# we may be repeating the weights. But the algorithm does not go over the same
# weight twice. That's what is achieved through recurrence.
# How are the weights accrued/accumulated? since we don't see any check against that in the algorithm.
# algorithm just checks whether the weight is equal to or less than the current capacity being considered.
# then it aims to tack on the previous answer from table matching capacity (b-wi), that is b - current weight being
# considered. If this answer is greater than previous, then it updates itself.
# in other words the weight accumulation is done via recurrence when considering the previous weights.
# and the constraint is that (b-wi) cannot be less than 0 since wi<=b
# so in both value addition and weight accumulation, the algorithm uses recurrence to achieve those.
# another thing, what guarantees recursion of K is that the capacity is large enough to subsume the various weights.
# for example, the way 10 is made up of 2 is that, 2 added 2 makes up 4. so 4 is K[2] + 2.
# K[6] = K[4] + 2, which is 2 + 2 + 2. and so on.
def knapsack(B, V, W):
    K = [0 for x in range(0, W)]
    print K
    for b in range(0, W):
        print "Capacity:{}".format(b)
        for i in range(0, len(B)):
            wi = B[i]
            poss_K = V[i] + K[b - wi]
            print "\t\tb = {} wi = {} (b-wi) = {}  possible_K = {}".format(b, wi,(b-wi), poss_K)
            if wi <= b and K[b] < poss_K:
                K[b] = poss_K
    print K


if __name__ == '__main__':
    B = [2, 3, 4, 6]
    V = [9, 16, 14, 30]
    W = 10  # knapsack capacity
    knapsack(B, V, W)
