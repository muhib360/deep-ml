import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    X = np.array(X);
    unit_X = np.nan_to_num(X / np.sqrt(np.sum(X ** 2, axis=1, keepdims=True)), copy=False)

    return unit_X @ unit_X.T