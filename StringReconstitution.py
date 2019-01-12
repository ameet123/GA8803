words = ["it", "was", "the", "best", "of", "times"]


def dict(w):
    return True if w in words else False


def reconstitute(s):
    S = [s[0]]
    remaining = ["" for _ in s]
    remaining[0] = "" if dict(s[0]) else s[0]

    print "Len of s:{} r:{}".format(len(s), len(remaining))
    for i in range(1, len(s)):
        c = remaining[i - 1] + s[i]
        if not dict(c):
            remaining[i] = c
    for i, r in enumerate(remaining):
        print "{}->{}".format(i, r)


if __name__ == '__main__':
    s = "itwasthebestoftimes"
    reconstitute(s)
