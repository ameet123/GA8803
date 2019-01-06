def maxSum_subsequence(a):
    S = [a[0]]
    seq = [[a[0]]]
    for i in range(1, len(a)):
        # print (">>Processing index:{} val:{} seq #:{} i-1:{} S[i-1]:{}".format(i, a[i], len(seq), seq[i - 1],
        # S[i - 1]))
        if S[i - 1] < 0:
            S.insert(i, a[i])
            seq.insert(i, [a[i]])
        else:
            S.insert(i, a[i] + S[i - 1])
            b = list(seq[i - 1])
            b.append(a[i])
            seq.insert(i, b)
    max_sum = -999
    max_seq = []
    for i in range(0, len(a)):
        if S[i] > max_sum:
            max_sum = S[i]
            max_seq = seq[i]
        print ("[{}]:\t{}\t\t==>{}".format(a[i], seq[i], S[i]))
    print ("MAX sum:{} max Seq:{}".format(max_sum, max_seq))


if __name__ == '__main__':
    a = [5, 15, -30, 10, -5, 40, 10]
    maxSum_subsequence(a)
