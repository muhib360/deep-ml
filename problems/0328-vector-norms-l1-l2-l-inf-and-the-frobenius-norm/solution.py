import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    NORM_MAP = {
        "l1": 1,
        "l2": 2,
        "linf": np.inf,
        "frobenius": 'fro',
    }

    is_valid_norm = norm_type in NORM_MAP

    if norm_type not in NORM_MAP:
        raise ValueError(f"Unsupported norm_type '{norm_type}'")
    
    ord_val = NORM_MAP[norm_type]

    if norm_type == "frobenius" and arr.ndim != 2:
        raise ValueError("Frobenius norm requires a 2D array")
    
    if norm_type != "frobenius":
        arr = arr.flatten()

    return np.linalg.norm(arr, ord=ord_val)

