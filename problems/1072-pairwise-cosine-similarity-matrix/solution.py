import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.array(X);
    unit_X = X / np.sqrt(np.sum(X ** 2, axis=1, keepdims=True))

    np.nan_to_num(unit_X, copy=False)

    return unit_X @ unit_X.T