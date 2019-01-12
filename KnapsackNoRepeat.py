import numpy as np

def knapsack(B, V, W):
    K = np.zeros((len(B) + 1, W + 1)).astype(int)
    print K.shape

    for i in range(0, len(B)):
        wi = B[i]
        vi = V[i]
        for b in range(1, W + 1):
            prev_val_inc = K[i][b - wi]  # capacity decreased, since this guy included
            prev_val = K[i][b]  # capacity same since this guy is not included
            if wi <= b:
                poss = vi + prev_val_inc
                if poss > prev_val:
                    K[i + 1][b] = poss
                else:
                    K[i + 1][b] = prev_val
            else:
                K[i + 1][b] = prev_val
    print K


if __name__ == '__main__':
    B = [2, 3, 4, 6]
    V = [9, 16, 14, 30]
    W = 10  # knapsack capacity
    knapsack(B, V, W)
