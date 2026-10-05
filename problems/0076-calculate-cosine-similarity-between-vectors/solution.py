import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape == v2.shape and np.linalg.norm(v1) and np.linalg.norm(v2):
		dot_prod = v1 @ v2
		mags = np.linalg.norm(v1) * np.linalg.norm(v2)
		return dot_prod / mags