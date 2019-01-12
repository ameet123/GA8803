import numpy as np

def makeValue(B, W):
    K = np.zeros((len(B) + 1, W + 1)).astype(int)
    print K.shape

    for i in range(0, len(B)):
        wi = B[i]
        for b in range(1, W + 1):
            prev_val_inc = K[i][b - wi]  # capacity decreased, since this guy included
            prev_val = K[i][b]  # capacity same since this guy is not included
            if wi <= b:
                K[i + 1][b] = max(wi + prev_val_inc, prev_val)
            else:
                K[i + 1][b] = prev_val
    print K


if __name__ == '__main__':
    B = [2, 3, 4]
    W = 10  # knapsack capacity
    makeValue(B, W)
