import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	MODE_MAP = {
		'row': 1,
		'column': 0
	}
	return np.mean(matrix, axis = MODE_MAP[mode])